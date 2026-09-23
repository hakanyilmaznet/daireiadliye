<?php
/**
 * Dâire-i Adliyye - Kullanıcı Kimlik Doğrulama API'si (api/auth.php)
 */

require_once __DIR__ . '/config.php';

$action = $_GET['action'] ?? $_POST['action'] ?? 'me';

switch ($action) {
    case 'register':
        handleRegister();
        break;
    case 'login':
        handleLogin();
        break;
    case 'logout':
        handleLogout();
        break;
    case 'me':
    default:
        handleMe();
        break;
}

/**
 * Yeni Kullanıcı Kaydı
 */
function handleRegister() {
    $input = getJsonInput();
    $username = trim($input['username'] ?? '');
    $email = trim($input['email'] ?? '');
    $password = $input['password'] ?? '';

    if (empty($username) || empty($email) || empty($password)) {
        jsonResponse([
            'success' => false,
            'error'   => 'Kullanıcı adı, e-posta ve şifre zorunludur.'
        ], 400);
    }

    if (strlen($username) < 3 || strlen($username) > 50) {
        jsonResponse([
            'success' => false,
            'error'   => 'Kullanıcı adı 3 ile 50 karakter arasında olmalıdır.'
        ], 400);
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        jsonResponse([
            'success' => false,
            'error'   => 'Geçerli bir e-posta adresi giriniz.'
        ], 400);
    }

    if (strlen($password) < 6) {
        jsonResponse([
            'success' => false,
            'error'   => 'Şifre en az 6 karakter olmalıdır.'
        ], 400);
    }

    $pdo = getDbConnection();

    // Kullanıcı adı veya e-posta kullanımda mı kontrol et
    $stmt = $pdo->prepare("SELECT id FROM users WHERE username = ? OR email = ? LIMIT 1");
    $stmt->execute([$username, $email]);
    if ($stmt->fetch()) {
        jsonResponse([
            'success' => false,
            'error'   => 'Bu kullanıcı adı veya e-posta adresi zaten kayıtlı.'
        ], 409);
    }

    $hash = password_hash($password, PASSWORD_BCRYPT);
    $stmt = $pdo->prepare("INSERT INTO users (username, email, password_hash, created_at, last_login_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)");
    $stmt->execute([$username, $email, $hash]);
    $userId = (int)$pdo->lastInsertId();

    // Oturumu başlat
    $_SESSION['user_id'] = $userId;
    $_SESSION['username'] = $username;
    $_SESSION['email'] = $email;

    jsonResponse([
        'success' => true,
        'message' => 'Kayıt başarılı. Hoş geldiniz!',
        'user'    => [
            'id'       => $userId,
            'username' => $username,
            'email'    => $email
        ]
    ], 201);
}

/**
 * Kullanıcı Girişi
 */
function handleLogin() {
    $input = getJsonInput();
    $login = trim($input['username'] ?? $input['email'] ?? '');
    $password = $input['password'] ?? '';

    if (empty($login) || empty($password)) {
        jsonResponse([
            'success' => false,
            'error'   => 'Kullanıcı adı/e-posta ve şifre gereklidir.'
        ], 400);
    }

    $pdo = getDbConnection();
    $stmt = $pdo->prepare("SELECT id, username, email, password_hash FROM users WHERE username = ? OR email = ? LIMIT 1");
    $stmt->execute([$login, $login]);
    $user = $stmt->fetch();

    if (!$user || !password_verify($password, $user['password_hash'])) {
        jsonResponse([
            'success' => false,
            'error'   => 'Kullanıcı adı veya şifre hatalı.'
        ], 401);
    }

    // Son giriş zamanını güncelle
    $upStmt = $pdo->prepare("UPDATE users SET last_login_at = CURRENT_TIMESTAMP WHERE id = ?");
    $upStmt->execute([$user['id']]);

    // Oturumu başlat
    $_SESSION['user_id'] = (int)$user['id'];
    $_SESSION['username'] = $user['username'];
    $_SESSION['email'] = $user['email'];

    jsonResponse([
        'success' => true,
        'message' => 'Giriş başarılı.',
        'user'    => [
            'id'       => (int)$user['id'],
            'username' => $user['username'],
            'email'    => $user['email']
        ]
    ]);
}

/**
 * Kullanıcı Çıkışı
 */
function handleLogout() {
    $_SESSION = [];
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(session_name(), '', time() - 42000,
            $params["path"], $params["domain"],
            $params["secure"], $params["httponly"]
        );
    }
    session_destroy();

    jsonResponse([
        'success' => true,
        'message' => 'Oturum sonlandırıldı.'
    ]);
}

/**
 * Aktif Kullanıcı Bilgisi ve İstatistikleri
 */
function handleMe() {
    $userId = getCurrentUserId();
    if (!$userId) {
        jsonResponse([
            'success'   => true,
            'logged_in' => false,
            'user'      => null
        ]);
    }

    $pdo = getDbConnection();
    $stmt = $pdo->prepare("SELECT id, username, email, created_at, last_login_at FROM users WHERE id = ? LIMIT 1");
    $stmt->execute([$userId]);
    $user = $stmt->fetch();

    if (!$user) {
        // Oturumdaki kullanıcı veritabanında yoksa oturumu sil
        session_destroy();
        jsonResponse([
            'success'   => true,
            'logged_in' => false,
            'user'      => null
        ]);
    }

    // Kullanıcının kayıtlı ilerlemeleri ve toplam cevap sayısı
    $progStmt = $pdo->prepare("SELECT era, turn_number, stat_justice, stat_people, stat_treasury, stat_military, stat_authority, is_game_over, updated_at FROM game_progress WHERE user_id = ?");
    $progStmt->execute([$userId]);
    $progressList = $progStmt->fetchAll();

    $ansStmt = $pdo->prepare("SELECT COUNT(*) AS total_answers FROM user_answers WHERE user_id = ?");
    $ansStmt->execute([$userId]);
    $ansRow = $ansStmt->fetch();

    jsonResponse([
        'success'   => true,
        'logged_in' => true,
        'user'      => [
            'id'            => (int)$user['id'],
            'username'      => $user['username'],
            'email'         => $user['email'],
            'created_at'    => $user['created_at'],
            'last_login_at' => $user['last_login_at'],
            'total_answers' => (int)($ansRow['total_answers'] ?? 0),
            'progress'      => $progressList
        ]
    ]);
}
