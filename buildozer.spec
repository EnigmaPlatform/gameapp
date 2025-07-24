[app]
title = StatMaster
package.name = statmaster
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,json

version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[app_config]
orientation = portrait
fullscreen = 0

[buildozer_android]
# Android API target
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = true

# Android SDK
android.sdk = 31
android.ndk_path = 
android.sdk_path = 

# Gradle
android.gradle_dependencies = com.android.tools.build:gradle:7.2.1
android.enable_androidx = true

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Arch
android.arch = arm64-v8a

# Presplash
android.presplash_color = #0F1A2D
