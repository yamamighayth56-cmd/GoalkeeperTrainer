[app]

# اسم التطبيق
title = GoalkeeperTraining

# اسم الحزمة
package.name = goalkeepertraining

# الدومين
package.domain = org.goalkeeper

# مجلد المشروع
source.dir = .

# الملفات التي سيتم تضمينها
source.include_exts = py,png,jpg,jpeg,kv,atlas

# نسخة التطبيق
version = 1.0

# المكتبات المطلوبة
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

# شاشة كاملة
fullscreen = 0


# إعدادات Android
android.api = 35
android.minapi = 23

# إصدار NDK
android.ndk = 25b

# السماح باستخدام AndroidX
android.enable_androidx = True


[buildozer]

# مستوى السجلات
log_level = 2

# التحذير عند التشغيل بصلاحيات root
warn_on_root = 1
