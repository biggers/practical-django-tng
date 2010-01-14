from django.conf.urls.defaults import *
from cab.views.home import home

urlpatterns = patterns('',
    url(r'^$', home, name='cab_home'),
)
