from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterBaseForm

import main_app.recaptcha_simple

### Universal functions ###

### Captcha Section, leave only one of them. If former, you don't need to install recaptcha-client ###

### From here on is views: ###
def add_billing(request):
    if request.method == 'POST':

        response = main_app.recaptcha_simple.submit(request.POST.get('g-recaptcha-response'), request.META['REMOTE_ADDR'])
        #print "reCaptcha: " + request.POST.get('g-recaptcha-response')
        #print "remote: " + request.META['REMOTE_ADDR']
        #print response.is_valid

        if response.is_valid:
            # process your form now
            print "Form passed!"
            return render(request, 'user_details/add_billing_address.html', {})
        else:
            # return the form
            print "Form not passed. Recaptcha wrong."
            response = redirect('user_details:register')
            response['Location'] += '?fail=recaptcha'
            return response

def add_postal(request):
    return render(request, 'user_details/add_postal_address.html', {})


def register(request):
    return render(request, 'user_details/register_base.html', {})

def postal_done(request):
    return render(request, 'user_details/my-account', {})

def account(request):
    return render(request, 'user_details/account.html', {})

def simple_form(request):
    form = RegisterBaseForm()
    return render(request, 'user_details/simple_form.html', {'form' : form})
