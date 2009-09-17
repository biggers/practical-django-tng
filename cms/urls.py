from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
     { 'document_root': '/Users/jbennett/Sites/tiny_mce/' }),
    (r'^search/$', 'cms.search.views.search'),
    (r'^weblog/$', 'coltrane.views.entries_index'),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/', 'coltrane.views.entry_detail'),
    (r'', include('django.contrib.flatpages.urls')),
)
