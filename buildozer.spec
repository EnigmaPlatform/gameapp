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
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b  # Полный путь
android.sdk = 33
android.archs = arm64-v8a

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

# Оптимизации
android.no_ndk_build = False
android.accept_sdk_license = True
p4a.branch = develop
android.private_storage = True

# Логирование
log_level = 2

[buildozer]
# Конфигурация buildozer
log_level = 2
warn_on_root = 1
