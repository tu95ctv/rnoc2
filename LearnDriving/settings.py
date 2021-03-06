# Django settings for LearnDriving project.
import os
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH1 = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH1)


TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH,'static')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db3g2',                      # Or path to database file if using sqlite3.
        'USER': 'tu95ctv',                      # Not used with sqlite3.
        'PASSWORD': '228787',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
'''
DATABASES = {
             
             
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'df4jp6o8c1beqb',                      # Or path to database file if using sqlite3.
        
        
        'USER': 'ckraekaooavasz',                      # Not used with sqlite3.
        'PASSWORD': 'wFOKVHB09byG6pQC_mtLQFV3n1',                  # Not used with sqlite3.
        'HOST': 'ec2-54-83-202-115.compute-1.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
'''
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.


#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Bangkok'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') # Absolute path to the media directory

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJECT_PATH,'collect/static')
#CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
#CKEDITOR_UPLOAD_PATH = 'content/ckeditor/' 
'''
CKEDITOR_CONFIGS = {
    'default': {
        #'toolbar': 'full',
        'height': 80,
        'width': '100%',
    },
    'lenh_ckeditor': {
        #'toolbar': 'Basic',
        'height': 146,
        'width': '100%'
    },
}
'''
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_PATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%+n(a0=ej_6+*f$s)+n#6ts^h197x%en_p9wr4(mfbs=1x+pig'

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
    
    'django_tables2_reports.middleware.TableReportMiddleware',
    #'rnoc.middleware.TimezoneMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'LearnDriving.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'LearnDriving.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)
'''
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
                               #'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages',# ADD theo https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
                               'django.core.context_processors.static',# new add when add table report
                               )
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',# ADD theo https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
                'django.template.context_processors.static',
            ],
        }
    }
]


EXCEL_SUPPORT = 'xlwt' # or 'openpyxl' or 'pyexcelerator' # new add when add table report

INSTALLED_APPS = (
     
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable the admin:
    
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'rnoc',
    'django_tables2',
    #'wishlist',
    'crispy_forms',
    'django_tables2_reports',
    #'ckeditor',
    #'shop'
)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#WISHLIST_ITEM_MODEL = 'drivingtest.Linhkien'
LOGIN_REDIRECT_URL = '/omckv2/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
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
LOGIN_URL = '/login/'
MYD4_LOOKED_FIELD1 = {'site_name_1':'SN1', 'site_name_2':'SN2','site_ID_2G':'2G', 'site_id_3g':'3G'}

FORMAT_TIME = '%H:%M %d-%m-%Y'

AUTH_PROFILE_MODULE = "rnoc.UserProfile"
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'