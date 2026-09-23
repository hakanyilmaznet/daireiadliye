<?php
/**
 * Dâire-i Adliyye - Veritabanı ve API Yapılandırması (api/config.php)
 * Salt MySQL Veritabanı Mimarisi
 */

// 1. Hata Raporlama
error_reporting(E_ALL);
ini_set('display_errors', '0');

// Global İstisna Yakalayıcı (500 hatalarında boş sayfa dönmesini engeller)
set_exception_handler(function(Throwable $e) {
    if (!headers_sent()) {
        header("Content-Type: application/json; charset=UTF-8");
        http_response_code(500);
    }
    echo json_encode([
        'success' => false,
        'error'   => 'Sunucu Hatası: ' . $e->getMessage(),
        'code'    => 'INTERNAL_SERVER_ERROR'
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
});

// 2. Güvenli Oturum Başlatma
if (session_status() === PHP_SESSION_NONE && !headers_sent()) {
    @ini_set('session.cookie_httponly', '1');
    @ini_set('session.use_only_cookies', '1');
    @session_start();
}

// 3. CORS ve JSON Başlıkları
if (!headers_sent()) {
    header("Content-Type: application/json; charset=UTF-8");
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
}

if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') {
    if (!headers_sent()) http_response_code(200);
    exit;
}

// 4. Veritabanı Bağlantı Sabitleri (cPanel / Canlı MySQL)
define('DB_HOST', getenv('DB_HOST') ?: 'localhost');
define('DB_PORT', getenv('DB_PORT') ?: '3306');
define('DB_NAME', getenv('DB_NAME') ?: 'mukerre_daireiadliye');
define('DB_USER', getenv('DB_USER') ?: 'mukerre_daireiadliye');
define('DB_PASS', getenv('DB_PASS') ?: 'tAv_xibbhbPWe7R6');
define('DB_CHARSET', 'utf8mb4');

/**
 * PDO MySQL Veritabanı Bağlantısı (Singleton Pattern)
 */
function getDbConnection() {
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }

    try {
        $dsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
            PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES " . DB_CHARSET
        ];
        $pdo = new PDO($dsn, DB_USER, DB_PASS, $options);
        return $pdo;
    } catch (PDOException $e) {
        jsonResponse([
            'success' => false,
            'error'   => 'MySQL veritabanı bağlantı hatası: ' . $e->getMessage(),
            'code'    => 'DB_CONNECTION_ERROR'
        ], 500);
    }
}

/**
 * Standart JSON Yanıt Yardımcısı
 */
function jsonResponse($data, $statusCode = 200) {
    if (!headers_sent()) {
        http_response_code($statusCode);
    }
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

/**
 * İstemciden Gelen JSON Gövdesini Çözümleme
 */
function getJsonInput() {
    $raw = file_get_contents('php://input');
    if (empty($raw)) {
        return [];
    }
    $decoded = json_decode($raw, true);
    return is_array($decoded) ? $decoded : [];
}

/**
 * Aktif Kullanıcı ID'sini Döndürür
 */
function getCurrentUserId() {
    if (!empty($_SESSION['user_id'])) {
        return (int)$_SESSION['user_id'];
    }
    return null;
}

/**
 * Oturum Açılmış Olmasını Zorunlu Kılar
 */
function requireAuth() {
    $userId = getCurrentUserId();
    if (!$userId) {
        jsonResponse([
            'success' => false,
            'error'   => 'Bu işlem için üye girişi yapmanız gerekmektedir.',
            'code'    => 'UNAUTHORIZED'
        ], 401);
    }
    return $userId;
}
