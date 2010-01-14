from cab.models import Language, Snippet
from django.views.generic.list_detail import object_list

def top_authors(request):
    return object_list(request, queryset=Snippet.objects.top_authors(),
                        template_name='cab/top_authors.html',
                        paginate_by=20)

def top_languages(request):
    return object_list(request, queryset=Language.objects.top_languages(),
                        template_name='cab/top_languages.html',
                        paginate_by=20)

def most_bookmarked(request):
    return object_list(request, queryset=Snippet.objects.most_bookmarked(),
                        template_name='cab/most_bookmarked.html',
                        paginate_by=20)

def top_rated(request):
    return object_list(request, queryset=Snippet.objects.top_rated(),
                        template_name='cab/top_rated.html',
                        paginate_by=20)