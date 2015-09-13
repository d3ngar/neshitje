from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def homepage(request):

    return render(request, 'main_app/homepage.html', {})
    
