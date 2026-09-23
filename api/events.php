<?php
/**
 * Dâire-i Adliyye - Tekil Olay Çekim API'si (api/events.php)
 * Olaylar veritabanından tek tek çekilir (Stream/On-Demand).
 * Üyelik zorunludur.
 */

require_once __DIR__ . '/config.php';

$action = $_GET['action'] ?? 'next';
$era = $_GET['era'] ?? 'modern';
if (!in_array($era, ['modern', 'ottoman'])) {
    $era = 'modern';
}

switch ($action) {
    case 'get':
        handleGetEvent();
        break;
    case 'counts':
        handleEventCounts();
        break;
    case 'next':
    default:
        handleNextEvent($era);
        break;
}

/**
 * Sıradaki Tekil Olayı Getir (Üye Zorunlu)
 */
function handleNextEvent($era) {
    $userId = requireAuth(); // Misafir oynayamaz, üye girişi şart!
    $pdo = getDbConnection();
    $crisisKey = $_GET['crisis_key'] ?? null;
    $excludeId = $_GET['exclude_id'] ?? null;

    // 1. Toplam Vaka Sayısını Öğren
    $cntStmt = $pdo->prepare("SELECT COUNT(*) AS total FROM events WHERE era = ?");
    $cntStmt->execute([$era]);
    $totalCount = (int)($cntStmt->fetch()['total'] ?? 0);

    if ($totalCount === 0) {
        jsonResponse([
            'success' => false,
            'error'   => 'Veritabanında henüz bu döneme ait olay bulunmamaktadır. Lütfen install.php dosyasını çalıştırınız.',
            'code'    => 'NO_EVENTS_FOUND'
        ], 404);
    }

    // 2. Kullanıcının Oynadığı Olay ID'lerini Bul
    $ansStmt = $pdo->prepare("SELECT DISTINCT event_id FROM user_answers WHERE user_id = ? AND era = ?");
    $ansStmt->execute([$userId, $era]);
    $playedIds = $ansStmt->fetchAll(PDO::FETCH_COLUMN);

    // Eğer istemci şu an gösterilen olayı hariç tutmak istediyse
    if ($excludeId && !in_array($excludeId, $playedIds)) {
        $playedIds[] = $excludeId;
    }

    // Eğer tüm olaylar oynanmışsa döngüyü sıfırla
    if (count($playedIds) >= $totalCount) {
        $playedIds = $excludeId ? [$excludeId] : [];
    }

    // 3. Henüz oynanmamış adayları sorgula
    $params = [$era];
    $sql = "SELECT id, era, title, source, `desc`, characters_json, options_json, sort_order 
            FROM events 
            WHERE era = ?";

    if (!empty($playedIds)) {
        $placeholders = implode(',', array_fill(0, count($playedIds), '?'));
        $sql .= " AND id NOT IN ($placeholders)";
        $params = array_merge($params, $playedIds);
    }

    // Kriz filtresi varsa (%70 şansla kriz anahtar kelimelerini arat)
    $crisisKeywords = [
        'treasury' => ['hazine', 'akçe', 'vergi', 'maliye', 'bütçe', 'döviz', 'enflasyon', 'sarraf', 'faiz'],
        'military' => ['ordu', 'asker', 'yeniçeri', 'güvenlik', 'savunma', 'terör', 'tsk', 'sefer', 'sınır'],
        'justice'  => ['adalet', 'kadı', 'mahkeme', 'hukuk', 'rüşvet', 'yargı', 'şaibe', 'yolsuzluk', 'delil'],
        'people'   => ['reaya', 'köylü', 'halk', 'deprem', 'afet', 'sağlık', 'esnaf', 'tüketici', 'barınma'],
        'authority'=> ['mülk', 'otorite', 'darbe', 'muhalefet', 'vesayet', 'isyan', 'sadrazam', 'meclis']
    ];

    $matchedEvent = null;

    if ($crisisKey && isset($crisisKeywords[$crisisKey]) && (mt_rand(1, 100) <= 70)) {
        $kwList = $crisisKeywords[$crisisKey];
        $kwConditions = [];
        $kwParams = $params;
        foreach ($kwList as $kw) {
            $kwConditions[] = "(`title` LIKE ? OR `desc` LIKE ? OR `source` LIKE ?)";
            $kwParams[] = "%$kw%";
            $kwParams[] = "%$kw%";
            $kwParams[] = "%$kw%";
        }
        $crisisSql = $sql . " AND (" . implode(" OR ", $kwConditions) . ") ORDER BY RAND() LIMIT 1";
        $cStmt = $pdo->prepare($crisisSql);
        $cStmt->execute($kwParams);
        $matchedEvent = $cStmt->fetch();
    }

    // Kriz eşleşmesi yoksa rastgele bir unplayed olay çek
    if (!$matchedEvent) {
        $sql .= " ORDER BY RAND() LIMIT 1";
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        $matchedEvent = $stmt->fetch();
    }

    // Hiçbir şey bulunamazsa fallback olarak herhangi birini getir
    if (!$matchedEvent) {
        $fallbackStmt = $pdo->prepare("SELECT id, era, title, source, `desc`, characters_json, options_json FROM events WHERE era = ? ORDER BY RAND() LIMIT 1");
        $fallbackStmt->execute([$era]);
        $matchedEvent = $fallbackStmt->fetch();
    }

    if (!$matchedEvent) {
        jsonResponse([
            'success' => false,
            'error'   => 'Olay getirilemedi.'
        ], 404);
    }

    // JSON alanlarını çöz
    $characters = json_decode($matchedEvent['characters_json'], true) ?: [];
    $options = json_decode($matchedEvent['options_json'], true) ?: [];

    jsonResponse([
        'success'      => true,
        'played_count' => count($playedIds),
        'total_count'  => $totalCount,
        'event'        => [
            'id'         => $matchedEvent['id'],
            'era'        => $matchedEvent['era'],
            'title'      => $matchedEvent['title'],
            'source'     => $matchedEvent['source'],
            'desc'       => $matchedEvent['desc'],
            'characters' => $characters,
            'options'    => $options
        ]
    ]);
}

/**
 * Belirli bir Olayı ID ile Getir (Üye Zorunlu)
 */
function handleGetEvent() {
    requireAuth();
    $id = trim($_GET['id'] ?? '');
    if (empty($id)) {
        jsonResponse(['success' => false, 'error' => 'Olay ID gereklidir.'], 400);
    }

    $pdo = getDbConnection();
    $stmt = $pdo->prepare("SELECT id, era, title, source, `desc`, characters_json, options_json FROM events WHERE id = ? LIMIT 1");
    $stmt->execute([$id]);
    $ev = $stmt->fetch();

    if (!$ev) {
        jsonResponse(['success' => false, 'error' => 'Olay bulunamadı.'], 404);
    }

    jsonResponse([
        'success' => true,
        'event'   => [
            'id'         => $ev['id'],
            'era'        => $ev['era'],
            'title'      => $ev['title'],
            'source'     => $ev['source'],
            'desc'       => $ev['desc'],
            'characters' => json_decode($ev['characters_json'], true) ?: [],
            'options'    => json_decode($ev['options_json'], true) ?: []
        ]
    ]);
}

/**
 * Dönem Bazında Toplam Olay Sayıları
 */
function handleEventCounts() {
    $pdo = getDbConnection();
    $stmt = $pdo->query("SELECT era, COUNT(*) AS count FROM events GROUP BY era");
    $rows = $stmt->fetchAll();

    $counts = ['modern' => 0, 'ottoman' => 0];
    foreach ($rows as $r) {
        $counts[$r['era']] = (int)$r['count'];
    }

    jsonResponse([
        'success' => true,
        'counts'  => $counts
    ]);
}
