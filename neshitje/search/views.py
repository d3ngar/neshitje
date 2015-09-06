from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def search(request):

    return render(request, 'search/search.html', {})


def search_results(request):

    return render(request, 'search/results.html', {})
