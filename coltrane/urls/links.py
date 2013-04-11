from django.conf.urls.defaults import *

from coltrane.models import Link
from django.views.generic.dates import DateDetailView

link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.dates',
    (r'^$', DateDetailView.get_object, link_info_dict, 'coltrane_link_archive_index'),
    
    (r'^(?P<year>\d{4})/$', DateDetailView.get_year, link_info_dict, 'coltrane_link_archive_year'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', DateDetailView.get_month, link_info_dict, 'coltrane_link_archive_month'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DateDetailView.get_day, link_info_dict, 'coltrane_link_archive_day'),
    
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view, link_info_dict, 'coltrane_link_detail'),

)
