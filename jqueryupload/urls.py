from django.conf.urls.defaults import *

from jqueryupload.views import multiuploader_delete

urlpatterns = patterns('',
    (r'^delete/(\d+)/$', multiuploader_delete),
    url(r'^$', 'jqueryupload.views.image_view', name='main'),
    url(r'^multiuploader/$', 'jqueryupload.views.multiuploader', name='multi'),
    
)
