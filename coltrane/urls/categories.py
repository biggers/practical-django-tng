from django.conf.urls.defaults import patterns, url

from coltrane.models import Category
from django.views.generic.list import ListView

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(queryset=Category.objects.all()),
        name='coltrane_category_list'),

    url(r'^(?P<slug>[-\w]+)/$', 'coltrane.views.category_detail', {},
        name='coltrane_category_detail'),
)
