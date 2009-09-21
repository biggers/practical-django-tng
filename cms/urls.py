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
    (r'^weblog/$',
     'django.views.generic.date_based.archive_index',
     entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/$',
     'django.views.generic.date_based.archive_year',
     entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$',
     'django.views.generic.date_based.archive_month',
     entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'django.views.generic.date_based.archive_day',
     entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'django.views.generic.date_based.object_detail',
     entry_info_dict),
    (r'', include('django.contrib.flatpages.urls')),
)
