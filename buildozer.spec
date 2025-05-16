[app]

# Основные настройки приложения
title = Геймификация повседневности
package.name = gamificationoflife
package.domain = org.gamification
source.dir = .
source.main = main.py
version = 0.1

# Android специфичные настройки
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_path = %(source.dir)s/.buildozer/android/platform/android-ndk-r25b
android.sdk = 33
android.archs = arm64-v8a
android.skip_update = True  # Отключаем автоматическое обновление SDK/NDK

# Разрешения
android.permissions = INTERNET

# Пути к ресурсам
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,xml
source.include_patterns = assets/*
icon.filename = assets/icons/free-icon-unicorn-4431575.png

# Ориентация и графика
orientation = portrait
fullscreen = 0
android.opengl = 2

# Зависимости
requirements = 
    python3,
    kivy==2.2.1,
    openssl,
    pyjnius,
    android,
    kivymd==1.1.1,
    libffi

# Дополнительные настройки Android
android.allow_backup = True
android.adaptive_icon_foreground = assets/icons/free-icon-unicorn-4431575.png
android.wakelock = False
android.private_storage = True

# Оптимизации
android.no_ndk_build = False
android.accept_sdk_license = True
p4a.branch = develop
android.release_artifact = %(source.dir)s/bin/  # Путь для сохранения APK

# Настройки сборки
[buildozer]
log_level = 2
warn_on_root = 1

# Настройки для релизной сборки (раскомментируйте для подписи APK)
#[app:release]
#key.alias = release
#key.store.password = 
#key.store = 
#key.password = 

# Настройки Google Play (опционально)
#android.google_play_key = 
#android.google_play_track = internal  # или production
