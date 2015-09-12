from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def add_billing(request):

    return render(request, 'user_data/add_billing_address.html', {})

def add_postal(request):

    return render(request, 'user_data/add_billing_address.html', {})
