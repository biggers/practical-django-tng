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
    'django.contrib.comments',
    'django.contrib.syndication',
#    'django.contrib.flatpages',
    'coltrane',
    'django_pygments',
    'cab',
    'taggit',
    'flatpage_views',
    'help',
    #for fluent contents
    'fluent_contents',
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    'fluent_contents.plugins.disquswidgets',
    'fluent_contents.plugins.formdesignerlink',
    'fluent_contents.plugins.gist',
    'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.text',
    'disqus',
    'django_wysiwyg',
    'form_designer',
    # MUST be the last (after all apps!)
    'upload',
    'south',
    'flatpages_plus',
    'layouts',
)
MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES + (
#    'flatpages_plus.middleware.FlatpageFallbackMiddleware',
    # South (migrations) MUST be the last, after all apps!
#    'south',
)

#MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES  + (
#    'flatpages_plus.middleware.FlatpageFallbackMiddleware',
#)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
DISQUS_API_KEY = 'WiO5bxw1OfVJq4jLbi5HY96FkZEtn3Ju09Ua9egTQfo2Uty3JKFchzkcMRrJeVk4'
DISQUS_WEBSITE_SHORTNAME = 'fhndemo.net'

import os, sys

import django.views.debug

def wing_debug_hook(*args, **kwargs):
    if __debug__ and 'WINGDB_ACTIVE' in os.environ:
        exc_type, exc_value, traceback = sys.exc_info()
        sys.excepthook(exc_type, exc_value, traceback)
    return old_technical_500_response(*args, **kwargs)

old_technical_500_response = django.views.debug.technical_500_response
django.views.debug.technical_500_response = wing_debug_hook
