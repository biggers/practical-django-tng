from cab.models import Language, Snippet
#from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView

def top_authors(request):
    return ListView.as_view(request, queryset=Snippet.objects.top_authors(),
                            template_name='cab/top_authors.html',
                            paginate_by=20)

def top_languages(request):
    return ListView.as_view(request, queryset=Language.objects.top_languages(),
                            template_name='cab/top_languages.html',
                            paginate_by=20)

def most_bookmarked(request):
    return ListView.as_view(request, queryset=Snippet.objects.most_bookmarked(),
                            template_name='cab/most_bookmarked.html',
                            paginate_by=20)

def top_rated(request):
    return ListView.as_view(request, queryset=Snippet.objects.top_rated(),
                            template_name='cab/top_rated.html',
                            paginate_by=20)
