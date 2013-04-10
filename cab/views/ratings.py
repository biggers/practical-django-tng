from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from cab.models import Rating, Snippet

def rate(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if 'rating' not in request.GET or request.GET['rating'] not in ('1', '-1'):
        return HttpResponseRedirect(snippet.get_absolute_url())
    try:
        rating = Rating.objects.get(user__pk=request.user.id, snippet__pk=snippet.id)
    except Rating.DoesNotExist:
        rating = Rating(user=request.user, snippet=snippet)
    rating.rating = int(request.GET['rating'])
    rating.save()
    return HttpResponseRedirect(snippet.get_absolute_url())
rate = login_required(rate)