import os

from pathlib import Path
from corsheaders.defaults import default_headers
import dj_database_url






# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-it@6n&vxwrw(irst+)7@o-uxrs+er6ctho0*pn=7-&36@mb&j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tokenix.onrender.com', 'localhost', '127.0.0.1', 'tokenix24.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'corsheaders',
    'channels',
]



CORS_ALLOW_ALL_ORIGINS = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
]

ROOT_URLCONF = 'dashboard_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'dashboard' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard_project.wsgi.application'
ASGI_APPLICATION = 'dashboard_project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # default for local development


DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'tokenix',
#         'USER': 'tokenix_user',
#         'PASSWORD': 'RqSwNClWye7KA0E2Gp1npS8jOYu70K7q',
#         'HOST': 'tokenix.onrender.com',  # Render database host address
#         'PORT': '5432',      # Default PostgreSQL port
#     }
# }
# # You can also explicitly specify the ENGINE as follows:
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Directories to find static files during development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Points to your development static folder
]

# STATIC_ROOT = BASE_DIR / "staticfiles" 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'  # Set the desired redirect URL after login

LOGIN_URL = 'login'  # Set the login page URL
LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CSRF_COOKIE_NAME = 'csrftoken'
# CSRF_COOKIE_SECURE = True  # Set to True if using HTTPS
# CSRF_COOKIE_SAMESITE = 'Strict' 

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default
CSRF_USE_SESSIONS = True  # Ensure CSRF tokens are stored in sessions
SESSION_COOKIE_SECURE = True  # Set to True in production with HTTPS



OPAY_MERCHANT_ID = '281824061140739'
OPAY_SECRET_KEY = 'OPAYPRV17181044296430.8961471637244277'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'dashboard': {  # Replace 'dashboard' with the name of your app
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# vbdQGyUSxk7XDuKT

