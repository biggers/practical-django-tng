from django.conf.urls.defaults import *
from django.contrib import admin

from coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

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
    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags/', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),
    (r'', include('django.contrib.flatpages.urls')),
)
