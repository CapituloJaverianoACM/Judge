import os
import sys

DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

SITE_NAME = os.path.basename(DJANGO_ROOT)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'run', 'static')

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'run', 'media')

sys.path.append(os.path.normpath(os.path.join(PROJECT_ROOT, 'apps')))

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'x^=!5h-r4vmtz&%&(fio!fnvdm3wpyc5n!r5a@o@&&tfaej@hy'
)

DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken'
]

LOCAL_APPS = [
    'business_judge.user',
    'business_judge.description',
    'business_judge.problem',
    'business_judge.submission',
    'business_judge.template',
    'business_judge.test_case',
    'utils'
]

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

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'mydatabase'),
        'USER': os.environ.get('DATABASE_USER', 'mydatabaseuser'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'mypassword'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

# TODO - is used?
'''
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'App.auth.model.ExpiringTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
'''


LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Bogota')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
