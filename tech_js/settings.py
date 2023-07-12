import json
import openai
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
with open('jsonForce.json') as secret_file:
    config = json.load(secret_file)
    SECRET_KEY = config['hashed_key']
    openai.api_key = config['ia']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'axes',
    'principal',
    'app_users',
    
    # 'corsheaders',
    # 'rest_framework',
    # 'rest_framework.authtoken',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [  # here order has its importance
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tech_js.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tech_js.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # djongo
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


# Default primary key field:  TO_RENDER_IN_MUCH_COMPLEX_WAYS_OF_CONFIGURATION
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Allow The Cross Origin Requests Server
# if not DEBUG:  # disable everyone to get the api/data
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',   # DjangoModelPermissionOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication'
    ),
    #'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JsonRender',)
}
"""
CORS_ORIGIN_WHITELIST = [
    r'http://127.0.0.1:3000',      # regular expression
    r'http://192.168.43.98:3000',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    r'http://localhost:3000',
    r'http://192.168.43.98:3000',
]
"""
AXES_FAILURE_LIMIT = 3
AXES_LOCK_OUT_AT_FAILURE = True
# AXES_COOLOFF_TIME = timedelta(minutes=15)
