[app]

title = GoalkeeperTraining
package.name = goalkeepertraining
package.domain = org.goalkeeper

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 24
android.ndk = 25b
android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a

android.enable_androidx = True
android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1
