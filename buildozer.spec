[app]
title = Goalkeeper Traini
package.name = goalkeeperapp
package.domain = org.goalkeeper
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,mp3,wav
version = 0.1
requirements = python3,kivy==2.3.0,gtts,arabic_reshaper,python-bidi
permissions = INTERNET,RECORD_AUDIO
android.api = 35
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.private_storage = True
android.copy_libs = 1
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
orientation = portrait
android.logcat_filters = *:S python:D
[buildozer]
log_level = 2
warn_on_root = 1
