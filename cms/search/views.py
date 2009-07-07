from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage


def search(request):
    query = request.GET.get('q', '')
    keyword_results = []
    results = []
    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',
                              { 'query': query,
                                'keyword_results': keyword_results,
                                'results': results })
