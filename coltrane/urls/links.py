from django.conf.urls.defaults import patterns, url
from django.views.generic.dates import DateDetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView

from coltrane.models import Link

urlpatterns = patterns('django.views.generic.dates',
    url(r'^$',
        ArchiveIndexView.as_view(queryset=Link.objects.all(),
                                 date_field='pub_date'),
                                 name='coltrane_link_archive_index'),

    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(queryset=Link.objects.all(),
                                date_field='pub_date'),
                                name='coltrane_link_archive_year'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        MonthArchiveView.as_view(queryset=Link.objects.all(),
                                 date_field='pub_date'),
                                 name='coltrane_link_archive_month'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        DayArchiveView.as_view(queryset=Link.objects.all(),
                               date_field='pub_date'),
                               name='coltrane_link_archive_day'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(queryset=Link.objects.all(),
                               date_field='pub_date'),
                               name='coltrane_link_detail'),
                               
)
