<?php
/**
 * Dâire-i Adliyye - Veritabanı ve Deste Kurulum Sihirbazı (install.php)
 * Hem CLI (Terminal) hem de Web Tarayıcısı üzerinden çalışabilir.
 */

require_once __DIR__ . '/api/config.php';

// CLI veya Web kontrolü
$isCli = (php_sapi_name() === 'cli');

function outputMsg($msg, $type = 'info') {
    global $isCli;
    if ($isCli) {
        $prefix = $type === 'success' ? '✓ ' : ($type === 'error' ? '✗ ' : 'ℹ ');
        echo $prefix . strip_tags($msg) . PHP_EOL;
    } else {
        $color = $type === 'success' ? '#22c55e' : ($type === 'error' ? '#ef4444' : '#38bdf8');
        echo "<div style='margin: 6px 0; padding: 10px 14px; background: rgba(0,0,0,0.4); border-left: 4px solid $color; border-radius: 4px; font-family: monospace;'>$msg</div>";
        flush();
    }
}

if (!$isCli) {
    echo "<!DOCTYPE html>
    <html lang='tr'>
    <head>
        <meta charset='UTF-8'>
        <title>Dâire-i Adliyye - Veritabanı Kurulumu</title>
        <style>
            body { background: #0c1017; color: #f1f5f9; font-family: 'Segoe UI', system-ui, sans-serif; padding: 30px; max-width: 800px; margin: 0 auto; line-height: 1.6; }
            h1 { color: #f59e0b; border-bottom: 1px solid #334155; padding-bottom: 10px; font-size: 24px; }
            .btn { display: inline-block; background: #d97706; color: #fff; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 20px; transition: 0.2s; }
            .btn:hover { background: #f59e0b; }
            .box { background: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        </style>
    </head>
    <body>
    <div class='box'>
        <h1>🏛️ Dâire-i Adliyye: Veritabanı ve Vaka Kurulum Sihirbazı</h1>";
}

outputMsg("Veritabanı bağlantısı test ediliyor (Sunucu: " . DB_HOST . ", DB: " . DB_NAME . ")...");

try {
    // 1. Veritabanını oluşturmayı dene (varsa geçer)
    try {
        $rootDsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";charset=" . DB_CHARSET;
        $tempPdo = new PDO($rootDsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
        ]);
        $tempPdo->exec("CREATE DATABASE IF NOT EXISTS `" . DB_NAME . "` CHARACTER SET " . DB_CHARSET . " COLLATE utf8mb4_unicode_ci");
        outputMsg("Veritabanı '" . DB_NAME . "' hazır veya başarıyla oluşturuldu.", "success");
    } catch (Exception $e) {
        outputMsg("Veritabanı oluşturma adımı atlandı (Yetki kısıtı olabilir, mevcut veritabanına bağlanılıyor): " . $e->getMessage(), "info");
    }

    $pdo = getDbConnection();
    outputMsg("Veritabanına başarıyla bağlanıldı (MySQL).", "success");

    // 2. Tabloları oluştur (schema.sql)
    $schemaPath = __DIR__ . '/schema.sql';
    if (!file_exists($schemaPath)) {
        throw new Exception("schema.sql dosyası bulunamadı!");
    }
    outputMsg("MySQL tabloları oluşturuluyor (schema.sql çalıştırılıyor)...");
    $sqlContent = file_get_contents($schemaPath);
    $pdo->exec($sqlContent);
    outputMsg("users, events, game_progress ve user_answers tabloları hazır.", "success");

    // 3. Olayları events_data.sql dosyasından içe aktar
    $dataPath = __DIR__ . '/events_data.sql';
    if (file_exists($dataPath)) {
        outputMsg("2.000 vaka verisi içe aktarılıyor (events_data.sql)...");
        $handle = fopen($dataPath, "r");
        if ($handle) {
            $pdo->beginTransaction();
            $stmtCount = 0;
            $buffer = "";
            while (($line = fgets($handle)) !== false) {
                $trimmed = trim($line);
                if (empty($trimmed) || strpos($trimmed, '--') === 0 || strpos($trimmed, 'SET NAMES') === 0) {
                    continue;
                }
                $buffer .= $line;
                if (substr($trimmed, -1) === ';') {
                    $pdo->exec($buffer);
                    $buffer = "";
                    $stmtCount++;
                    if ($stmtCount % 250 === 0) {
                        $pdo->commit();
                        $pdo->beginTransaction();
                    }
                }
            }
            if ($pdo->inTransaction()) {
                $pdo->commit();
            }
            fclose($handle);
            outputMsg("✓ $stmtCount adet vaka sorgusu başarıyla çalıştırıldı.", "success");
        }
    }

    // 4. Güncel vaka sayılarını kontrol et
    $cntStmt = $pdo->query("SELECT era, COUNT(*) as cnt FROM events GROUP BY era");
    $counts = $cntStmt->fetchAll(PDO::FETCH_KEY_PAIR);
    $mCount = $counts['modern'] ?? 0;
    $oCount = $counts['ottoman'] ?? 0;
    outputMsg("Veritabanındaki toplam vaka durumu: Modern Türkiye = $mCount vaka, Klasik Osmanlı = $oCount vaka.", "success");

    // 5. Test Kullanıcısı Oluşturma (Demo)
    $userCheck = $pdo->query("SELECT COUNT(*) AS total FROM users")->fetch();
    if ((int)$userCheck['total'] === 0) {
        $demoPass = password_hash('adliye123', PASSWORD_BCRYPT);
        $userStmt = $pdo->prepare("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)");
        $userStmt->execute(['veziriazam', 'vezir@daireiadliye.gov.tr', $demoPass]);
        outputMsg("Örnek demo kullanıcı oluşturuldu: Kullanıcı: <b>veziriazam</b> | Şifre: <b>adliye123</b>", "info");
    }

    outputMsg("🎉 Tebrikler! Kurulum başarıyla tamamlandı. Artık olaylar doğrudan veritabanından tek tek çekilecek.", "success");

    if (!$isCli) {
        echo "<div style='text-align: center;'>
            <a href='index.html' class='btn'>🎮 Dâire-i Adliyye'ye Başla</a>
        </div>";
    }

} catch (Exception $e) {
    if (isset($pdo) && $pdo instanceof PDO && $pdo->inTransaction()) {
        $pdo->rollBack();
    }
    outputMsg("Kurulum sırasında hata oluştu: " . $e->getMessage(), "error");
}

if (!$isCli) {
    echo "</div></body></html>";
}
