"""
Django settings for wheelars project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import psycopg2
from django.contrib.messages import constants as messages
from django.urls  import reverse_lazy
import  dj_database_url
import whitenoise

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['WHEELARS_SECRET_KEY']
print(SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wheelars.herokuapp.com','wheelars.com','www.wheelars.com','localhost:8000','http://127.0.0.1:8000/','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'blog',
    'cars',
    'contact',
    'ckeditor',
    'multiselectfield',
    'mathfilters',
    'django.contrib.humanize',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'wheelars.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR +'/templates'],
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

WSGI_APPLICATION = 'wheelars.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'wheelarsprojdb',
#         'USER':'aacreetiee',
#         'PASSWORD' : 'aakuiloveu25!.',
#         'HOST':'localhost',
#         'PORT':'',
#     }
# }
DATABASES={
    'default':dj_database_url.config(default='postgres://aacreetiee:aakuiloveu25!.@localhost/wheelarsprojdb')
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'wheelars/static')
]
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MESSAGE_TAGS={
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.ERROR: 'danger',
    messages.DEBUG:'debug',
    50:'critical',
}
SITE_ID=3
DEFAULT_HTTP_PROTOCOL = "https"
LOGIN_REDIRECT_URL = reverse_lazy('accounts:dashboard')

LOGIN_URL= reverse_lazy('accounts:login')

#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='sudhanregmi25@gmail.com'
EMAIL_HOST_PASSWORD=os.environ.get('S_GMAIL_P')
EMAIL_USE_TLS=True

#whitenose setup
STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
