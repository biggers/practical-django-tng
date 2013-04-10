from django.conf.urls.defaults import *
from cab.models import Snippet
from tagging.models import Tag


urlpatterns = patterns('',
    (r'^(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', { 
        'queryset_or_model': Snippet.objects.all(), 
        'template_name': 'cab/snippets_by_tag.html'
    }, 'cab_snippet_archive_tag'),
)