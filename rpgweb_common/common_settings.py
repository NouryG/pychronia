# -*- coding: utf-8 -*-

import sys, os, tempfile, random, logging, re

try:
    import PIL.Image # that monolithic package has been exploded in several packages now
    sys.modules['Image'] = PIL.Image # WORKAROUND - prevents "AccessInit: hash collision: 3 for both 1 and 1"
except ImportError:
    pass


import rpgweb_common.default_logging_config

##################### SETTINGS TO BE OVERRIDDEN BY DEPLOYMENT-SPECIFIC CONF FILE ####################

SITE_ID = None
SECRET_KEY = None

SESSION_COOKIE_DOMAIN = None # eg. ".mydomain.net"

SERVER_EMAIL = DEFAULT_FROM_EMAIL = ""
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = ""
EMAIL_USE_TLS = False


ROOT_URLCONF = None

DEBUG = False
TEMPLATE_DEBUG = False

SITE_DOMAIN = None # NO trailing slash, used to build absolute urls


######################################################################################################


ugettext = lambda s: s # dummy placeholder for makemessages


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # base folder where rpgweb packages are stored


SESSION_COOKIE_NAME = 'sessionid' # DO NOT CHANGE - needed for phpbb integration

MEDIA_URL = '/static/media/' # examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH, "media") # for uploaded files, generated docs etc.

STATIC_URL = "/static/resources/"
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/' # deprecated but required by djangocms
STATIC_ROOT = os.path.join(ROOT_PATH, "_static_files") # where collectstatic cmd will place files
STATICFILES_DIRS = ()

TIME_ZONE = 'Europe/Paris'
USE_L10N = True
USE_I18N = True
LANGUAGE_CODE = 'fr'
LANGUAGES = (
  ('fr', ugettext('French')),
  ('en', ugettext('English')),
)
LOCALE_PATHS = () # in addition to application-local "locale/" dirs


APPEND_SLASH = True # so handy for mistyped urls...


IGNORABLE_404_URLS = (# ONLY SOON IN 1.5
    re.compile(r'\.(php|cgi)$'),
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = () # use absolute paths here, not relative paths.
TEMPLATE_STRING_IF_INVALID = "" # or "<INVALID %s>" to debug

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    #"django.contrib.messages.context_processors.messages" - we use our own version
    "sekizai.context_processors.sekizai",
)



MIDDLEWARE_CLASSES = (
#'django.middleware.common.BrokenLinkEmailsMiddleware', ONLY SOON IN 1.5
'sessionprofile.middleware.SessionProfileMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',

# 'localeurl.middleware.LocaleURLMiddleware',
# 'django.middleware.locale.LocaleMiddleware', replaced by LocaleURLMiddleware
'django.middleware.common.CommonMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',

'debug_toolbar.middleware.DebugToolbarMiddleware',
)




# to be extended in specific settings #
INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # only these sessions are scalable for "sharding"
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.staticfiles',

    'south',
    'debug_toolbar',
    'sekizai',
    'django_wsgiserver', # uses cherrypy

    'sessionprofile', # keeps track of sessions/users in DB table, for PHPBB integration
    'templateaddons', # assign and headers tags
    'django_select2', # advanced select box
    'easy_thumbnails',

    'rpgweb_common', # common templates, tags, static files etc.

]


## activate django-sentry if present ##
try:
    import sentry.client
    INSTALLED_APPS.append('sentry.client')
except ImportError:
    pass # sentry is optional



############# DJANGO-APP CONFS ############


## DJANGO-SELECT2 CONF ##
AUTO_RENDER_SELECT2_STATICS = False


## DJANGO CONTRIB MESSAGES CONF ##
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG # minimum recorded level
# Set MESSAGE_TAGS setting if needed, to control corresponding CSS classes


## DJANGO DEBUG TOOLBAR CONF ##
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda *args, **kwargs: True, # always, at the moment
    'ENABLE_STACKTRACES' : True,
    'HIDE_DJANGO_SQL': True,
    'SHOW_TEMPLATE_CONTEXT': True,
}


## DJANGO CONTRIB RST CONF ##
RESTRUCTUREDTEXT_FILTER_SETTINGS = {"initial_header_level": 2, # minimum "h2" when rendered to html
                                    "doctitle_xform": False, # important, to have even lone titles stay in the html fragment
                                    "sectsubtitle_xform": False,
                                    'file_insertion_enabled': False,  # SECURITY MEASURE (file hacking)
                                    'raw_enabled': False, } # SECURITY MEASURE (script tag)

## EASY-THUMBNAILS CONF ##
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop', # superseded by "scale_and_crop_with_subject_location"
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
