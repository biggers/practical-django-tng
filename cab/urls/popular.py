from django.conf.urls.defaults import *
from cab.views import popular

urlpatterns = patterns('',
    url(r'^authors/$',
        popular.top_authors,
        name='cab_top_authors'),
        
    url(r'^languages/$',
        popular.top_languages,
        name='cab_top_languages'),
    
    url(r'^bookmarks/$', popular.most_bookmarked, name='cab_most_bookmarked'),
    
    url(r'^ratings/$', popular.top_rated, name='cab_top_rated'),
    
)