<?php
/**
 * Dâire-i Adliyye - Oyun İlerlemesi ve Hüküm Kayıt API'si (api/game.php)
 * Kullanıcının her cevabı veritabanına kaydedilir.
 * Üyelik zorunludur.
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
    $userId = requireAuth();
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
                             ORDER BY id DESC LIMIT 20");
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
 * Verilen Hükmü ve Güncel Durumu Kaydet (Her Cevap Kaydedilir)
 */
function handleSaveAnswer() {
    $userId = requireAuth();
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

    // 2. game_progress tablosunu güncelle / upsert et (MySQL)
    $justice   = (int)($stats['justice'] ?? 60);
    $people    = (int)($stats['people'] ?? 60);
    $treasury  = (int)($stats['treasury'] ?? 50);
    $military  = (int)($stats['military'] ?? 55);
    $authority = (int)($stats['authority'] ?? 60);
    $traitsJson = json_encode($traits, JSON_UNESCAPED_UNICODE);

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

    jsonResponse([
        'success'     => true,
        'message'     => 'Hüküm ve ilerleme başarıyla kaydedildi.',
        'turn_number' => $turnNumber
    ]);
}

/**
 * Kullanıcı İlerlemesini Sıfırla (Yeniden Başlama)
 */
function handleResetProgress($era) {
    $userId = requireAuth();
    $pdo = getDbConnection();

    $stmt = $pdo->prepare("DELETE FROM game_progress WHERE user_id = ? AND era = ?");
    $stmt->execute([$userId, $era]);

    jsonResponse([
        'success' => true,
        'message' => 'İlerleme sıfırlandı.'
    ]);
}

/**
 * Kullanıcının Geçmiş Hüküm Günlükleri
 */
function handleHistory($era) {
    $userId = requireAuth();
    $pdo = getDbConnection();

    $stmt = $pdo->prepare("SELECT turn_number, event_id, choice_label, log_text, effects_json, created_at 
                           FROM user_answers 
                           WHERE user_id = ? AND era = ? 
                           ORDER BY id DESC LIMIT 50");
    $stmt->execute([$userId, $era]);
    $history = $stmt->fetchAll();

    foreach ($history as &$h) {
        $h['effects'] = json_decode($h['effects_json'], true) ?: [];
        unset($h['effects_json']);
    }

    jsonResponse([
        'success' => true,
        'history' => $history
    ]);
}
