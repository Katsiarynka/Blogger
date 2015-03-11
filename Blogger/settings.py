#coding: utf-8
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'blogger.sql',  # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

CSRF_FAILURE_VIEW = True
ALLOWED_HOSTS = []
TIME_ZONE = 'Europe/Minsk'

BLOCKED_USERNAME = []
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath('./media/')
FILES_ROOT = os.path.abspath('./files/')

ADMIN_MEDIA_PREFIX = '/admin-media/'
STATIC_ROOT = os.path.abspath('./static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)


SECRET_KEY = '!t5%#m@9ri6o-sj(vj+u*xz1hs@bf$uc)z1#t0a-xc7s!u#i=#'

# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Blogger.urls'

WSGI_APPLICATION = 'Blogger.wsgi.application'



INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'django.contrib.admin',
    'tinymce',
    'djcelery',
    'apps',
    'apps.comments',
    'apps.posts',
    'apps.profiles',
    'apps.likes',
    'apps.tags',
    'apps.notes',
    'apps.partners',
    'south',
    "djcelery",
    'djkombu'
)

import djcelery
djcelery.setup_loader()
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TEMPLATE_DIRS = (
    os.path.abspath('./templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'django.core.context_processors.i18n'
    )

ADMIN_TOOLS_MENU = 'menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

import djcelery
djcelery.setup_loader()