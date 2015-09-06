from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def product(request):

    return render(request, 'product/product.html', {})
