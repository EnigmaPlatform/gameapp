[app]
title = StatMaster
package.name = statmaster
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,json

version = 0.2
requirements = python3,kivy

[buildozer]
log_level = 2

[app_config]
orientation = portrait

[buildozer_android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = true
android.arch = arm64-v8a
