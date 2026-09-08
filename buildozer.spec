[app]

# اسم التطبيق
title = Goalkeeper Trainer

# اسم الحزمة
package.name = goalkeepertrainer

# نطاق الحزمة
package.domain = org.goalkeeper

# مكان ملفات التطبيق
source.dir = .

# الملفات التي تدخل في APK
source.include_exts = py,png,jpg,jpeg,kv,atlas

# إصدار التطبيق
version = 1.0

# مكتبات Python المطلوبة
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

# شاشة كاملة
fullscreen = 0


[buildozer]

# مستوى سجل البناء
log_level = 2

# مكان ملفات البناء
warn_on_root = 1


[android]

# معمارية الأجهزة
android.archs = arm64-v8a

# إصدار Android الأدنى
android.minapi = 23

# إصدار Android المستهدف
android.api = 35

# اسم APK الناتج
android.accept_sdk_license = True
