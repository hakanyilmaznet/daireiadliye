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
        <h1>🏛️ Dâire-i Adliyye: Veritabanı ve Deste Kurulum Sihirbazı</h1>";
}

outputMsg("Veritabanı bağlantısı test ediliyor (Sunucu: " . DB_HOST . ", DB: " . DB_NAME . ")...");

try {
    // 1. Veritabanını oluşturmayı dene (varsa geçer)
    $rootDsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";charset=" . DB_CHARSET;
    $tempPdo = new PDO($rootDsn, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
    ]);
    $tempPdo->exec("CREATE DATABASE IF NOT EXISTS `" . DB_NAME . "` CHARACTER SET " . DB_CHARSET . " COLLATE utf8mb4_unicode_ci");
    outputMsg("Veritabanı '" . DB_NAME . "' hazır veya başarıyla oluşturuldu.", "success");
} catch (Exception $e) {
    outputMsg("Veritabanı oluşturma adımı atlandı (Yetki kısıtı olabilir, mevcut veritabanına bağlanılıyor): " . $e->getMessage(), "info");
}

try {
    $pdo = getDbConnection();
    outputMsg("Veritabanına başarıyla bağlanıldı.", "success");

    $driverName = $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);

    // 2. Tabloları oluştur
    if ($driverName === 'mysql') {
        $schemaPath = __DIR__ . '/schema.sql';
        if (!file_exists($schemaPath)) {
            throw new Exception("schema.sql dosyası bulunamadı!");
        }
        outputMsg("MySQL tabloları oluşturuluyor (schema.sql çalıştırılıyor)...");
        $sqlContent = file_get_contents($schemaPath);
        $pdo->exec($sqlContent);
    }
    outputMsg("users, events, game_progress ve user_answers tabloları hazır.", "success");

    // 3. Olayları JSON dosyalarından oku ve aktar
    function parseDeckFile($filePath) {
        if (!file_exists($filePath)) return [];
        $content = file_get_contents($filePath);
        $start = strpos($content, '[');
        $end = strrpos($content, ']');
        if ($start === false || $end === false) return [];
        $jsonStr = substr($content, $start, $end - $start + 1);
        $arr = json_decode($jsonStr, true);
        return is_array($arr) ? $arr : [];
    }

    if ($driverName === 'sqlite') {
        $insertStmt = $pdo->prepare("INSERT OR REPLACE INTO events (id, era, title, source, `desc`, characters_json, options_json, sort_order) 
            VALUES (:id, :era, :title, :source, :desc, :chars, :opts, :sort)");
    } else {
        $insertStmt = $pdo->prepare("INSERT INTO events (id, era, title, source, `desc`, characters_json, options_json, sort_order) 
            VALUES (:id, :era, :title, :source, :desc, :chars, :opts, :sort)
            ON DUPLICATE KEY UPDATE 
                title = VALUES(title),
                source = VALUES(source),
                `desc` = VALUES(`desc`),
                characters_json = VALUES(characters_json),
                options_json = VALUES(options_json),
                sort_order = VALUES(sort_order)");
    }

    // A. Modern Türkiye Destesi (1.000 Vaka)
    $modernFile = __DIR__ . '/event_deck_modern.json';
    if (!file_exists($modernFile)) {
        $modernFile = __DIR__ . '/event_deck_modern.js';
    }
    outputMsg("Modern Türkiye destesi okunuyor ($modernFile)...");
    $modernEvents = parseDeckFile($modernFile);
    outputMsg("Modern destede " . count($modernEvents) . " olay bulundu. Veritabanına aktarılıyor...");

    $pdo->beginTransaction();
    $mCount = 0;
    foreach ($modernEvents as $idx => $ev) {
        if (empty($ev['id']) || empty($ev['title'])) continue;
        $insertStmt->execute([
            ':id'     => $ev['id'],
            ':era'    => 'modern',
            ':title'  => $ev['title'],
            ':source' => $ev['source'] ?? 'Devlet Brifingi',
            ':desc'   => $ev['desc'] ?? '',
            ':chars'  => json_encode($ev['characters'] ?? [], JSON_UNESCAPED_UNICODE),
            ':opts'   => json_encode($ev['options'] ?? [], JSON_UNESCAPED_UNICODE),
            ':sort'   => $idx + 1
        ]);
        $mCount++;
    }
    $pdo->commit();
    outputMsg("✓ $mCount adet Modern Türkiye olayı veritabanına kaydedildi/güncellendi.", "success");

    // B. Klasik Osmanlı Destesi
    $ottomanFile = __DIR__ . '/event_deck.json';
    if (!file_exists($ottomanFile)) {
        $ottomanFile = __DIR__ . '/event_deck.js';
    }
    outputMsg("Klasik Osmanlı destesi okunuyor ($ottomanFile)...");
    $ottomanEvents = parseDeckFile($ottomanFile);
    outputMsg("Osmanlı destesinde " . count($ottomanEvents) . " olay bulundu. Veritabanına aktarılıyor...");

    $pdo->beginTransaction();
    $oCount = 0;
    foreach ($ottomanEvents as $idx => $ev) {
        if (empty($ev['id']) || empty($ev['title'])) continue;
        $insertStmt->execute([
            ':id'     => $ev['id'],
            ':era'    => 'ottoman',
            ':title'  => $ev['title'],
            ':source' => $ev['source'] ?? 'Dîvân-ı Hümâyûn Maruzu',
            ':desc'   => $ev['desc'] ?? '',
            ':chars'  => json_encode($ev['characters'] ?? [], JSON_UNESCAPED_UNICODE),
            ':opts'   => json_encode($ev['options'] ?? [], JSON_UNESCAPED_UNICODE),
            ':sort'   => $idx + 1
        ]);
        $oCount++;
    }
    $pdo->commit();
    outputMsg("✓ $oCount adet Klasik Osmanlı olayı veritabanına kaydedildi/güncellendi.", "success");

    // 4. Test Kullanıcısı Oluşturma (Demo)
    $userCheck = $pdo->query("SELECT COUNT(*) AS total FROM users")->fetch();
    if ((int)$userCheck['total'] === 0) {
        $demoPass = password_hash('adliye123', PASSWORD_BCRYPT);
        $userStmt = $pdo->prepare("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)");
        $userStmt->execute(['veziriazam', 'vezir@daireiadliye.gov.tr', $demoPass]);
        outputMsg("Örnek demo kullanıcı oluşturuldu: Kullanıcı: <b>veziriazam</b> | Şifre: <b>adliye123</b>", "info");
    }

    outputMsg("🎉 Tebrikler! Kurulum başarıyla tamamlandı. Artık olaylar veritabanından tek tek çekilecek.", "success");

    if (!$isCli) {
        echo "<div style='text-align: center;'>
            <a href='index.html' class='btn'>🎮 Dâire-i Adliyye'ye Başla</a>
        </div>";
    }

} catch (Exception $e) {
    if ($pdo && $pdo->inTransaction()) {
        $pdo->rollBack();
    }
    outputMsg("Kurulum sırasında hata oluştu: " . $e->getMessage(), "error");
}

if (!$isCli) {
    echo "</div></body></html>";
}
