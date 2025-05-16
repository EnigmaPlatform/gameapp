[app]

# Основные настройки
title = Геймификация повседневности
package.name = gamificationoflife
package.domain = org.gamification
source.dir = .
source.main = main.py
version = 0.1

# Настройки Android
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = %(source.dir)s/.buildozer/android/platform/android-sdk
android.build_tools_version = 34.0.0
android.platform = 33
android.archs = arm64-v8a
android.skip_update = True

# Разрешения
android.permissions = INTERNET

# Ресурсы
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,xml
source.include_patterns = assets/*
icon.filename = assets/icons/free-icon-unicorn-4431575.png

# Графика
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

# Дополнительные настройки
android.allow_backup = True
android.wakelock = False
android.accept_sdk_license = True
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
