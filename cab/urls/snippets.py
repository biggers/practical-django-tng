from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.views.generic.list_detail import object_list, object_detail

from cab.models import Snippet
from cab.views.snippets import add_snippet, edit_snippet


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(queryset=Snippet.objects.all(),
                         paginate_by=20),
                         name='cab_snippet_list'),

    url(r'^(?P<object_id>\d+)/$',
        DetailView.as_view(queryset=Snippet.objects.all()
                           ),
                           name='cab_snippet_detail'),

    url(r'^add/$',
        add_snippet,
        name='cab_snippet_add'),

    url(r'^edit/(?P<snippet_id>\d+)/$',
        edit_snippet,
        name='cab_snippet_edit'),
)
