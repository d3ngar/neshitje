from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterBaseForm, UserRegForm
from django.contrib import auth
from django.core.context_processors import csrf

import main_app.recaptcha_simple

### Universal functions ###

### Captcha Section, leave only one of them. If former, you don't need to install recaptcha-client ###

### From here on is views: ###
def add_billing(request):
    return render(request, 'user_details/add_billing_address.html', {})

def add_postal(request):
    return render(request, 'user_details/add_postal_address.html', {})

def login_process(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        response = redirect('user_details:account')
        return response
    else:
        response = redirect('user_details:register')
        return response

def logout_process(request):
    auth.logout(request)
    return redirect('main_app:homepage')

def register(request):
    if request.method == 'POST':
        #print request
        response = main_app.recaptcha_simple.submit(request.POST.get('g-recaptcha-response'), request.META['REMOTE_ADDR'])
        if response.is_valid:
            form = UserRegForm(request.POST)
            if form.is_valid():
                print "User reg form success"
                form.save()
                if request.POST.get('details') == 'submit':
                    response = redirect('user_details:add-billing')
                else:
                    response = redirect('user_details:account')
                return response
            else:
                return render(request, 'user_details/register_base.html', {'form' : form})
        else:
            # return the form
            print "Form not passed. Recaptcha wrong."
            response = redirect('user_details:register')
            response['Location'] += '?fail=recaptcha'
            return response

    form = UserRegForm()
    return render(request, 'user_details/register_base.html', {'form' : form})



def postal_done(request):
    return render(request, 'user_details/account.html', {})

def account(request):
    return render(request, 'user_details/account.html', {})


## This one is mainly to try around in.
def simple_form(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            print "User reg form success"
            form.save()
            response = redirect('user_details:account')
            return response
        else:
            return render(request, 'user_details/simple_form.html', {'form' : form})

    form = UserRegForm()
    return render(request, 'user_details/simple_form.html', {'form' : form})
