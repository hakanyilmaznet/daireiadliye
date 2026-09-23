<?php
/**
 * Dâire-i Adliyye - Veritabanı ve API Yapılandırması
 */

// 1. Hata Raporlama (Canlıda 0 yapılabilir)
error_reporting(E_ALL);
ini_set('display_errors', '0');

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

// 4. Veritabanı Bağlantı Sabitleri
// cPanel veya yerel sunucunuzun MySQL bilgilerine göre düzenleyebilirsiniz:
define('DB_DRIVER', getenv('DB_DRIVER') ?: 'mysql');
define('DB_HOST', getenv('DB_HOST') ?: 'localhost');
define('DB_PORT', getenv('DB_PORT') ?: '3306');
define('DB_NAME', getenv('DB_NAME') ?: 'mukerre_daireiadliye');
define('DB_USER', getenv('DB_USER') ?: 'mukerre_daireiadliye');
define('DB_PASS', getenv('DB_PASS') ?: 'tAv_xibbhbPWe7R6');
define('DB_CHARSET', 'utf8mb4');

/**
 * PDO Veritabanı Bağlantısı (Singleton Pattern)
 * cPanel'de doğrudan MySQL kullanılır; yerel geliştirme için SQLite yedekliliği desteklenir.
 */
function getDbConnection() {
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }

    $availableDrivers = class_exists('PDO') ? PDO::getAvailableDrivers() : [];

    // 1. MySQL Denemesi
    if (in_array('mysql', $availableDrivers) && DB_DRIVER !== 'sqlite') {
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
            // Eğer SQLite mevcut değilse veya açıkça MySQL isteniyorsa hata fırlat
            if (!in_array('sqlite', $availableDrivers)) {
                jsonResponse([
                    'success' => false,
                    'error'   => 'MySQL veritabanı bağlantı hatası: ' . $e->getMessage(),
                    'code'    => 'DB_CONNECTION_ERROR'
                ], 500);
            }
        }
    }

    // 2. SQLite Yedekliliği (Yerel veya Çevrimdışı Geliştirme İçin)
    if (in_array('sqlite', $availableDrivers)) {
        try {
            $sqliteFile = __DIR__ . '/daireiadliye.sqlite';
            $isNew = !file_exists($sqliteFile);
            $pdo = new PDO("sqlite:" . $sqliteFile, null, null, [
                PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
            ]);

            if ($isNew) {
                // Tabloları otomatik ilklendir
                $pdo->exec("CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_login_at DATETIME
                )");
                $pdo->exec("CREATE TABLE IF NOT EXISTS events (
                    id TEXT PRIMARY KEY,
                    era TEXT NOT NULL,
                    title TEXT NOT NULL,
                    source TEXT NOT NULL,
                    desc TEXT NOT NULL,
                    characters_json TEXT NOT NULL,
                    options_json TEXT NOT NULL,
                    sort_order INTEGER DEFAULT 0,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )");
                $pdo->exec("CREATE TABLE IF NOT EXISTS game_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    era TEXT NOT NULL,
                    turn_number INTEGER NOT NULL DEFAULT 1,
                    current_event_id TEXT,
                    stat_justice INTEGER NOT NULL DEFAULT 60,
                    stat_people INTEGER NOT NULL DEFAULT 60,
                    stat_treasury INTEGER NOT NULL DEFAULT 50,
                    stat_military INTEGER NOT NULL DEFAULT 55,
                    stat_authority INTEGER NOT NULL DEFAULT 60,
                    traits_json TEXT,
                    is_game_over INTEGER NOT NULL DEFAULT 0,
                    game_over_reason TEXT,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(user_id, era)
                )");
                $pdo->exec("CREATE TABLE IF NOT EXISTS user_answers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    era TEXT NOT NULL,
                    event_id TEXT NOT NULL,
                    turn_number INTEGER NOT NULL,
                    choice_index INTEGER NOT NULL,
                    choice_label TEXT NOT NULL,
                    effects_json TEXT NOT NULL,
                    log_text TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )");
            }

            return $pdo;
        } catch (PDOException $e) {
            jsonResponse([
                'success' => false,
                'error'   => 'Veritabanı bağlantı hatası: ' . $e->getMessage(),
                'code'    => 'DB_CONNECTION_ERROR'
            ], 500);
        }
    }

    jsonResponse([
        'success' => false,
        'error'   => 'Sistemde ne MySQL ne de SQLite PDO sürücüsü bulunamadı. Lütfen PHP PDO eklentisini etkinleştiriniz.',
        'code'    => 'NO_PDO_DRIVER'
    ], 500);
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
    // Opsiyonel: Header'da iletilen Bearer token veya misafir takibi için
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
            'error'   => 'Bu işlem için giriş yapmanız gerekmektedir.',
            'code'    => 'UNAUTHORIZED'
        ], 401);
    }
    return $userId;
}
