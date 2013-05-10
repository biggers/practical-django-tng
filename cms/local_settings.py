import os

# http://www.robgolding.com/blog/2010/05/03/extending-settings-variables-with-local_settings-py-in-django/#comment-284944491
class Settings(object):
    def __init__(self):
        import settings
        self.settings = settings
    def __getattr__(self, name):
        return getattr(self.settings, name)

settings = Settings()

INSTALLED_APPS = settings.INSTALLED_APPS + (
    'tinymce',
    'tagging',
    'cms.search',
    'django.contrib.markup',
#    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.syndication',
    'coltrane',
    'django_pygments',
    'cab',
    'flatpages_plus',
    'taggit',
    # MUST be the last (after all apps!)
    'south',
    'uploader.upload'
)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

import os, sys

import django.views.debug

def wing_debug_hook(*args, **kwargs):
    if __debug__ and 'WINGDB_ACTIVE' in os.environ:
        exc_type, exc_value, traceback = sys.exc_info()
        sys.excepthook(exc_type, exc_value, traceback)
    return old_technical_500_response(*args, **kwargs)

old_technical_500_response = django.views.debug.technical_500_response
django.views.debug.technical_500_response = wing_debug_hook
