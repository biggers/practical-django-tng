from django.conf.urls.defaults import *

from coltrane.models import Entry, Link
from tagging.models import Tag


urlpatterns = patterns('',
    (r'^$',
     'django.views.generic.list_detail.object_list',
     { 'queryset': Tag.objects.all() }),
    (r'^entries/(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     { 'queryset_or_model': Entry,
       'template_name': 'coltrane/entries_by_tag.html' }),
    (r'^links/(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     { 'queryset_or_model': Link,
       'template_name': 'coltrane/links_by_tag.html' }),
)
