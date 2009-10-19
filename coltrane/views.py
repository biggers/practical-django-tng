from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from coltrane.models import Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return object_list(request, queryset=category.entry_set.all(),
                       extra_context={ 'category': category })
