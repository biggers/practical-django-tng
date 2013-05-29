import os
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import settings
from coltrane.feeds import CategoryFeed, LatestEntriesFeed

admin.autodiscover()

feeds = {'entries': LatestEntriesFeed,
         'categories': CategoryFeed}

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tiny_mce/', include('tinymce.urls')),

    # url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
    #     { 'document_root': settings.PROJECT_ROOT + '/js/tiny_mce/' }),

    url(r'^search/$', 'cms.search.views.search'),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^weblog/categories/', include('coltrane.urls.categories')),
    url(r'^weblog/links/', include('coltrane.urls.links')),
    url(r'^weblog/tags/', include('coltrane.urls.tags')),
    url(r'^weblog/', include('coltrane.urls.entries'),name='weblog'),

    url(r'^weblog/feeds/(?P<url>.*)/$',
        'django.contrib.syndication.views.Feed', {'feed_dict': feeds}
        ),

    url(r'^codeshare/', include('cab.urls.home')),
    url(r'^codeshare/snippets/', include('cab.urls.snippets')),
    url(r'^codeshare/languages/', include('cab.urls.languages')),
    url(r'^codeshare/popular/', include('cab.urls.popular')),
    url(r'^codeshare/tags/', include('cab.urls.tags')),
    url(r'^codeshare/bookmarks/', include('cab.urls.bookmarks')),
    url(r'^codeshare/ratings/', include('cab.urls.ratings')),

    url(r'^codeshare/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.PROJECT_ROOT, 'cab', 'css') }),
    #url(r'^jqueryupload/', include('jqueryupload.urls')),
    url(r'^upload/', include('upload.urls')),

    url('^help/', include('flatpage_views.urls')),
    url('^help/list/', include('flatpage_views.urls')),
#    url(r'^pages/', include('layouts.urls')),
    url(r'^(?P<url>.*)/$', include('layouts.siteurls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)

