[app]

# Название приложения
title = Геймификация повседневности

# Имя пакета (должно быть уникальным)
package.name = gamificationoflife

# Домен (обратный DNS-формат)
package.domain = org.gamification

# Путь к основному файлу
source.dir = .

# Главный python-файл
source.main = main.py

# Версия приложения
version = 0.1

# Требуемая версия Android
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 33

# Разрешения
android.permissions = INTERNET

# Характеристики оборудования
android.features = 

# Библиотеки Python
requirements = python3,kivy==2.2.1

# Иконка (путь относительно корня)
icon.filename = assets/icons/free-icon-unicorn-4431575.png

# Ориентация экрана
orientation = portrait

# Полноэкранный режим
fullscreen = 0

# Включение OpenGL ES 2.0
android.opengl = 2

# В buildozer.spec
source.include_exts = py,png,jpg,kv,atlas,ttf
# В разделе [app]
android.arch = arm64-v8a

# В разделе требования
requirements = python3,kivy==2.2.1,openssl,pyjnius,android
