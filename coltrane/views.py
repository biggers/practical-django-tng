from django.shortcuts import render_to_response

from coltrane.models import Category


def category_list(request):
    return render_to_response('coltrane/category_list.html',
                              { 'object_list': Category.objects.all() })
