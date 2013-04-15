from django.conf.urls.defaults import patterns, url
from coltrane.models import Entry, Link
from tagging.models import Tag

from django.views.generic.list import ListView

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(queryset=Tag.objects.all(),
                         template_name='coltrane/tag_list.html'),
                         name='coltrane_tag_list'),

    url(r'^entries/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
        {'queryset_or_model': Entry.live.all(),
         'template_name': 'coltrane/entries_by_tag.html'},
         name='coltrane_entry_archive_tag'),

    url(r'^links/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
        {'queryset_or_model': Link.objects.all(),
         'template_name': 'coltrane/links_by_tag.html'},
         name='coltrane_link_archive_tag'),
)

