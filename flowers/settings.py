import os
from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان
SECRET_KEY = 'django-insecure-v-ts7mg!#^_4dp3df0*2vdpiwpns9kn2wxz$4wtjh5g*p)u0v0'

# وضع التطوير
DEBUG = True

# المضيفون المسموح لهم
ALLOWED_HOSTS = ['betla-flowers.onrender.com', 'localhost', '127.0.0.1']
# تم التعديل لتفعيل الموقع على Render


# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # ✅ تنسيق الأسعار والأرقام

    'flowers',  # ✅ تطبيقك الأساسي (استبدلي بـ 'flowers' إذا كان الاسم الفعلي)
]

# الوسطاء
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ يدعم السلة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف URLs الرئيسي
ROOT_URLCONF = 'flowers.urls'  # تأكدي أن اسم المشروع الرئيسي هو flowers

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ مجلد القوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ✅ مهم للهيدر
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'flowers.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق كلمة المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ملفات الوسائط (اختياري إن كنت سترفع صور لاحقًا)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# التوجيهات بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# الحقل الافتراضي للموديلات
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# دعم ملفات static عند DEBUG = False
STATIC_ROOT = BASE_DIR / 'staticfiles'

