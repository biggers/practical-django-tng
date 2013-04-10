from django.conf.urls.defaults import *
from django.contrib import admin
import settings # Needed for PROJECT_ROOT.
admin.autodiscover()

from coltrane.feeds import CategoryFeed, LatestEntriesFeed

feeds = { 'entries': LatestEntriesFeed,
          'categories': CategoryFeed }


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': settings.PROJECT_ROOT + '/js/tiny_mce/' }),

    (r'^search/$', 'cms.search.views.search'),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags/', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),
    
    (r'^weblog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),
     
    (r'^codeshare/', include('cab.urls.home')),
    (r'^codeshare/snippets/', include('cab.urls.snippets')),
    (r'^codeshare/languages/', include('cab.urls.languages')),
    (r'^codeshare/popular/', include('cab.urls.popular')),
    (r'^codeshare/tags/', include('cab.urls.tags')),
    (r'^codeshare/bookmarks/', include('cab.urls.bookmarks')),
    (r'^codeshare/ratings/', include('cab.urls.ratings')),
    
    (r'^codeshare/css/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.PROJECT_ROOT + '/../cab/css/' }),
 
    (r'', include('django.contrib.flatpages.urls')),
)
