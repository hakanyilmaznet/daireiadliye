<?php
/**
 * Dâire-i Adliyye - Oyun İlerlemesi ve Hüküm Kayıt API'si (api/game.php)
 */

require_once __DIR__ . '/config.php';

$action = $_GET['action'] ?? $_POST['action'] ?? 'progress';
$era = $_GET['era'] ?? $_POST['era'] ?? 'modern';
if (!in_array($era, ['modern', 'ottoman'])) {
    $era = 'modern';
}

switch ($action) {
    case 'save_answer':
        handleSaveAnswer();
        break;
    case 'reset_progress':
        handleResetProgress($era);
        break;
    case 'history':
        handleHistory($era);
        break;
    case 'progress':
    default:
        handleGetProgress($era);
        break;
}

/**
 * Kullanıcının Kayıtlı İlerlemesini Getir
 */
function handleGetProgress($era) {
    $userId = getCurrentUserId();

    if (!$userId) {
        // Misafir oturumunda session verisi var mı kontrol et
        $guestProgress = $_SESSION['guest_progress'][$era] ?? null;
        if ($guestProgress) {
            jsonResponse([
                'success'      => true,
                'is_logged_in' => false,
                'has_progress' => true,
                'progress'     => $guestProgress,
                'recent_logs'  => $_SESSION['guest_logs'][$era] ?? []
            ]);
        } else {
            jsonResponse([
                'success'      => true,
                'is_logged_in' => false,
                'has_progress' => false,
                'progress'     => null
            ]);
        }
    }

    $pdo = getDbConnection();
    $stmt = $pdo->prepare("SELECT turn_number, current_event_id, stat_justice, stat_people, stat_treasury, stat_military, stat_authority, traits_json, is_game_over, game_over_reason, updated_at 
                           FROM game_progress 
                           WHERE user_id = ? AND era = ? 
                           LIMIT 1");
    $stmt->execute([$userId, $era]);
    $row = $stmt->fetch();

    if (!$row) {
        jsonResponse([
            'success'      => true,
            'is_logged_in' => true,
            'has_progress' => false,
            'progress'     => null
        ]);
    }

    // Son kronik/hüküm günlüklerini de getir
    $logStmt = $pdo->prepare("SELECT turn_number, log_text, choice_label, created_at 
                             FROM user_answers 
                             WHERE user_id = ? AND era = ? 
                             ORDER BY id DESC LIMIT 15");
    $logStmt->execute([$userId, $era]);
    $recentLogs = array_reverse($logStmt->fetchAll());

    $progress = [
        'turn_number'      => (int)$row['turn_number'],
        'current_event_id' => $row['current_event_id'],
        'stats'            => [
            'justice'   => (int)$row['stat_justice'],
            'people'    => (int)$row['stat_people'],
            'treasury'  => (int)$row['stat_treasury'],
            'military'  => (int)$row['stat_military'],
            'authority' => (int)$row['stat_authority']
        ],
        'traits'           => json_decode($row['traits_json'], true) ?: ['adli' => 0, 'sulh' => 0, 'mali' => 0, 'otorite' => 0, 'nizam' => 0],
        'is_game_over'     => (bool)$row['is_game_over'],
        'game_over_reason' => $row['game_over_reason'],
        'updated_at'       => $row['updated_at']
    ];

    jsonResponse([
        'success'      => true,
        'is_logged_in' => true,
        'has_progress' => true,
        'progress'     => $progress,
        'recent_logs'  => $recentLogs
    ]);
}

/**
 * Verilen Hükmü ve Güncel Durumu Kaydet
 */
function handleSaveAnswer() {
    $input = getJsonInput();
    $era = $input['era'] ?? 'modern';
    if (!in_array($era, ['modern', 'ottoman'])) {
        $era = 'modern';
    }

    $eventId = trim($input['event_id'] ?? '');
    $turnNumber = (int)($input['turn_number'] ?? 1);
    $choiceIndex = (int)($input['choice_index'] ?? 0);
    $choiceLabel = trim($input['choice_label'] ?? '');
    $effects = $input['effects'] ?? [];
    $logText = trim($input['log'] ?? '');
    $stats = $input['stats'] ?? [];
    $traits = $input['traits'] ?? [];
    $isGameOver = !empty($input['is_game_over']) ? 1 : 0;
    $gameOverReason = trim($input['game_over_reason'] ?? '');
    $nextEventId = trim($input['next_event_id'] ?? '');

    $userId = getCurrentUserId();

    if ($userId) {
        $pdo = getDbConnection();

        // 1. Cevabı user_answers tablosuna ekle
        $ansStmt = $pdo->prepare("INSERT INTO user_answers (user_id, era, event_id, turn_number, choice_index, choice_label, effects_json, log_text, created_at) 
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)");
        $ansStmt->execute([
            $userId,
            $era,
            $eventId,
            $turnNumber,
            $choiceIndex,
            $choiceLabel,
            json_encode($effects, JSON_UNESCAPED_UNICODE),
            $logText
        ]);

        // 2. game_progress tablosunu güncelle / upsert et
        $justice   = (int)($stats['justice'] ?? 60);
        $people    = (int)($stats['people'] ?? 60);
        $treasury  = (int)($stats['treasury'] ?? 50);
        $military  = (int)($stats['military'] ?? 55);
        $authority = (int)($stats['authority'] ?? 60);
        $traitsJson = json_encode($traits, JSON_UNESCAPED_UNICODE);

        $driverName = $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);
        if ($driverName === 'sqlite') {
            $progSql = "INSERT OR REPLACE INTO game_progress 
                (user_id, era, turn_number, current_event_id, stat_justice, stat_people, stat_treasury, stat_military, stat_authority, traits_json, is_game_over, game_over_reason, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)";
        } else {
            $progSql = "INSERT INTO game_progress 
                (user_id, era, turn_number, current_event_id, stat_justice, stat_people, stat_treasury, stat_military, stat_authority, traits_json, is_game_over, game_over_reason, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON DUPLICATE KEY UPDATE 
                    turn_number = VALUES(turn_number),
                    current_event_id = VALUES(current_event_id),
                    stat_justice = VALUES(stat_justice),
                    stat_people = VALUES(stat_people),
                    stat_treasury = VALUES(stat_treasury),
                    stat_military = VALUES(stat_military),
                    stat_authority = VALUES(stat_authority),
                    traits_json = VALUES(traits_json),
                    is_game_over = VALUES(is_game_over),
                    game_over_reason = VALUES(game_over_reason),
                    updated_at = CURRENT_TIMESTAMP";
        }
        $progStmt = $pdo->prepare($progSql);
        $progStmt->execute([
            $userId,
            $era,
            $turnNumber,
            $nextEventId,
            $justice,
            $people,
            $treasury,
            $military,
            $authority,
            $traitsJson,
            $isGameOver,
            $gameOverReason
        ]);
    } else {
        // Misafir kullanıcı için session'a kaydet
        if (!isset($_SESSION['guest_progress'])) {
            $_SESSION['guest_progress'] = [];
        }
        $_SESSION['guest_progress'][$era] = [
            'turn_number'      => $turnNumber,
            'current_event_id' => $nextEventId,
            'stats'            => $stats,
            'traits'           => $traits,
            'is_game_over'     => (bool)$isGameOver,
            'game_over_reason' => $gameOverReason,
            'updated_at'       => date('Y-m-d H:i:s')
        ];

        if (!isset($_SESSION['guest_played'][$era])) {
            $_SESSION['guest_played'][$era] = [];
        }
        if ($eventId && !in_array($eventId, $_SESSION['guest_played'][$era])) {
            $_SESSION['guest_played'][$era][] = $eventId;
        }

        if (!isset($_SESSION['guest_logs'][$era])) {
            $_SESSION['guest_logs'][$era] = [];
        }
        $_SESSION['guest_logs'][$era][] = [
            'turn_number'  => $turnNumber,
            'log_text'     => $logText,
            'choice_label' => $choiceLabel,
            'created_at'   => date('Y-m-d H:i:s')
        ];
    }

    jsonResponse([
        'success' => true,
        'message' => 'Hüküm ve ilerleme başarıyla kaydedildi.',
        'saved'   => [
            'turn'  => $turnNumber,
            'event' => $eventId
        ]
    ]);
}

/**
 * Oyunu / İlerlemeyi Sıfırla
 */
function handleResetProgress($era) {
    $userId = getCurrentUserId();
    if ($userId) {
        $pdo = getDbConnection();
        // İlerlemeyi sil veya başlangıç değerlerine getir
        $stmt = $pdo->prepare("DELETE FROM game_progress WHERE user_id = ? AND era = ?");
        $stmt->execute([$userId, $era]);
    } else {
        unset($_SESSION['guest_progress'][$era]);
        $_SESSION['guest_played'][$era] = [];
        $_SESSION['guest_logs'][$era] = [];
    }

    jsonResponse([
        'success' => true,
        'message' => 'İlerleme sıfırlandı. Yeni saltanat / dönem başladı.'
    ]);
}

/**
 * Kullanıcının Geçmiş Hüküm Günlükleri
 */
function handleHistory($era) {
    $userId = getCurrentUserId();
    if (!$userId) {
        jsonResponse([
            'success' => true,
            'history' => $_SESSION['guest_logs'][$era] ?? []
        ]);
    }

    $pdo = getDbConnection();
    $stmt = $pdo->prepare("SELECT a.id, a.turn_number, a.event_id, a.choice_label, a.effects_json, a.log_text, a.created_at, e.title AS event_title 
                           FROM user_answers a 
                           LEFT JOIN events e ON a.event_id = e.id 
                           WHERE a.user_id = ? AND a.era = ? 
                           ORDER BY a.id ASC");
    $stmt->execute([$userId, $era]);
    $rows = $stmt->fetchAll();

    foreach ($rows as &$r) {
        $r['effects'] = json_decode($r['effects_json'], true);
        unset($r['effects_json']);
    }

    jsonResponse([
        'success' => true,
        'history' => $rows
    ]);
}
