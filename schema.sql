-- ==========================================================
-- Dâire-i Adliyye: Hüküm ve Nizam Simülatörü
-- MySQL Veritabanı Şeması (schema.sql)
-- ==========================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- 1. Kullanıcılar Tablosu
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `last_login_at` DATETIME NULL,
  INDEX `idx_username` (`username`),
  INDEX `idx_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Olaylar (Vakalar) Tablosu (Tekil Olay Akışı İçin)
CREATE TABLE IF NOT EXISTS `events` (
  `id` VARCHAR(50) NOT NULL PRIMARY KEY,
  `era` ENUM('ottoman', 'modern') NOT NULL DEFAULT 'modern',
  `title` VARCHAR(255) NOT NULL,
  `source` VARCHAR(255) NOT NULL,
  `desc` TEXT NOT NULL,
  `characters_json` LONGTEXT NOT NULL,
  `options_json` LONGTEXT NOT NULL,
  `sort_order` INT NOT NULL DEFAULT 0,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_era_sort` (`era`, `sort_order`),
  INDEX `idx_era_id` (`era`, `id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Kullanıcı İlerlemesi ve Son Kaldığı Yer (Game Progress)
CREATE TABLE IF NOT EXISTS `game_progress` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT NOT NULL,
  `era` ENUM('ottoman', 'modern') NOT NULL DEFAULT 'modern',
  `turn_number` INT NOT NULL DEFAULT 1,
  `current_event_id` VARCHAR(50) NULL,
  `stat_justice` INT NOT NULL DEFAULT 60,
  `stat_people` INT NOT NULL DEFAULT 60,
  `stat_treasury` INT NOT NULL DEFAULT 50,
  `stat_military` INT NOT NULL DEFAULT 55,
  `stat_authority` INT NOT NULL DEFAULT 60,
  `traits_json` TEXT NULL,
  `is_game_over` TINYINT(1) NOT NULL DEFAULT 0,
  `game_over_reason` VARCHAR(500) NULL,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `uk_user_era` (`user_id`, `era`),
  CONSTRAINT `fk_progress_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Kullanıcının Verdiği Hükümler / Cevaplar (Ruling Logs)
CREATE TABLE IF NOT EXISTS `user_answers` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT NOT NULL,
  `era` ENUM('ottoman', 'modern') NOT NULL DEFAULT 'modern',
  `event_id` VARCHAR(50) NOT NULL,
  `turn_number` INT NOT NULL,
  `choice_index` INT NOT NULL,
  `choice_label` TEXT NOT NULL,
  `effects_json` TEXT NOT NULL,
  `log_text` TEXT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_user_era_turn` (`user_id`, `era`, `turn_number`),
  INDEX `idx_user_event` (`user_id`, `era`, `event_id`),
  CONSTRAINT `fk_answers_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
