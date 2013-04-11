from django.conf.urls.defaults import *

from coltrane.models import Entry
from django.views.generic.dates import DateDetailView

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.dates',
    # 'django.views.generic.date_based',
    (r'^$', DateDetailView.get_object, entry_info_dict, 'coltrane_entry_archive_index'),

    (r'^(?P<year>\d{4})/$', DateDetailView.get_year, entry_info_dict, 'coltrane_entry_archive_year'),

    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', DateDetailView.get_month, entry_info_dict, 'coltrane_entry_archive_month'),

    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DateDetailView.get_day, entry_info_dict, 'coltrane_entry_archive_day'),

    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view, entry_info_dict, 'coltrane_entry_detail'),
)
