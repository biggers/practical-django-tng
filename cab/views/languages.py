from django.shortcuts import get_object_or_404
#from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView
from cab.models import Language

def language_detail(request, slug):
    language = get_object_or_404(Language, slug=slug)
    return  ListView.as_view(request,
                             queryset=language.snippet_set.all(),
                             paginate_by=20,
                             template_name='cab/language_detail.html',
                             extra_context={ 'language': language })
