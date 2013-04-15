from django.shortcuts import get_object_or_404
#from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView

from coltrane.models import Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return  ListView.as_view(queryset=category.live_entry_set(),
                             extra_context={'category': category})
