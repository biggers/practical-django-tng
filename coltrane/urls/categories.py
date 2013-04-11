from django.conf.urls.defaults import *

from coltrane.models import Category
from django.views.generic.list import ListView

urlpatterns = patterns('',
    (r'^$', ListView.as_view, { 'queryset': Category.objects.all() }, 'coltrane_category_list'),
    (r'^(?P<slug>[-\w]+)/$', 'coltrane.views.category_detail', {}, 'coltrane_category_detail'),
)
