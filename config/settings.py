from pathlib import Path
import environ
import os

env = environ.Env()
env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-91d0etxpbqzujy@ja*6z0tc6%%j-bpabi!b^8&xf&pzwemxek!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'cms',
    'import_export',
    'froala_editor',
    'blog',
    'django_browser_reload',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processor.allMetaTags'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True


#  Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# # Add this if you have a specific directory for static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')



CORS_ALLOWED_ORIGINS = [
    'https://empireofblogs.net',
    'http://empireofblogs.net',
    'http://195.110.59.253',
    'https://195.110.59.253',
    
]

CORS_ALLOWED_ORIGINS += ['http://localhost:3000',
'http://127.0.0.1:8000',
'http://127.0.0.1:3000',
'http://195.110.59.253',
    'https://195.110.59.253',
]


CORS_ORIGIN_WHITELIST = [
    u'https://empireofblogs.net',
    u'http://empireofblogs.net',
    u'http://195.110.59.253',
    u'https://195.110.59.253',
]


CORS_ORIGIN_WHITELIST += [
u'http://localhost:3000',
u'http://127.0.0.1:8000',
u'http://127.0.0.1:3000',
]


ALLOWED_HOSTS = ["*"]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CSRF_HEADER_NAME = "CSRF_COOKIE"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_NAME="csrftoken"
CSRF_HEADER_NAME="csrftoken"
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

CSRF_TRUSTED_ORIGINS = [
    'http://empireofblogs.net',
    'https://empireofblogs.net',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://195.110.59.253',
    'https://195.110.59.253',
]

DATA_UPLOAD_MAX_MEMORY_SIZE = 100000000000  # 1 GB
FILE_UPLOAD_MAX_MEMORY_SIZE = 100000000000  # 1 GB
