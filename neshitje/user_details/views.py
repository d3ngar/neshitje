from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import UserRegForm, BillingForm, PostalForm, LoginForm, ChangeEmailForm, ChangePasswordForm, ChangeNameForm
from .models import UserBilling, UserShipping

import main_app.recaptcha_simple

### Universal functions ###

### Captcha Section, leave only one of them. If former, you don't need to install recaptcha-client ###

### From here on is views: ###
def add_billing(request):
    if request.user.is_authenticated():
        user_id = request.user

        try:
            billing = UserBilling.objects.get(user_id=user_id, status=1)

            if billing is not None:
                if request.method == 'POST':
                    billing.status = 3
                    billing.save()
                    form = BillingForm(request.POST)
                    if form.is_valid():
                        form.save(user_id)
                        response = redirect('user_details:account')
                        return response
                form = BillingForm(instance=billing)
                return render(request, 'user_details/add_billing_address.html', {'form' : form})
        except:
            print "No billing address"

        if request.method == 'POST':
            form = BillingForm(request.POST)
            if form.is_valid():
                print "Billing success"
                form.save(user_id)

                if request.POST.get('save') == 'submit':
                    response = redirect('user_details:account')
                elif request.POST.get('add_shipping') == 'submit':
                    response = redirect('user_details:add-shipping')
                return response

            return render(request, 'user_details/add_billing_address.html', {'form' : form})
        else:
            form = BillingForm()
            return render(request, 'user_details/add_billing_address.html', {'form': form})

    else:
        response = redirect('user_details:logging')
        return response


def add_postal(request):
    if request.user.is_authenticated():
        user_id = request.user
        postals = UserShipping.objects.filter(user_id=user_id, status=1)

        if request.method == 'POST':
            form = PostalForm(request.POST)
            if form.is_valid():
                print "Postal success"
                form.save(user_id)
                response = redirect('user_details:account')
                return response

            return render(request, 'user_details/add_postal_address.html', {'form' : form, 'postals':postals})
        else:
            form = PostalForm()
            return render(request, 'user_details/add_postal_address.html', {'form': form, 'postals':postals})

    else:
        response = redirect('user_details:logging')
        return response


def logging(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
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
        else:
            return render(request, 'user_details/logging.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'user_details/logging.html', {'form': form})


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

def delete_postal(request):
    if request.method == 'GET':
        postal_id = request.GET.get('postal_id', None)
        post_add = UserShipping.objects.get(id=postal_id)
        post_add.status = 3
        post_add.save();
    return render(request, 'user_details/account.html', {})


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

def edit_email(request):
    if request.method == 'POST':
        user_id = request.user
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user = auth.authenticate(username=user_id.username, password=password)
            if user is not None:
                auth.login(request, user)
                user.email = email
                user.save()
                response = redirect('user_details:account')
                return response
            else:
                response = redirect('user_details:register')
                return response
        else:
            return render(request, 'user_details/edit_email.html', {'form':form, 'obj':'user_details:edit-email'})
    form = ChangeEmailForm()
    return render(request, 'user_details/edit_email.html', {'form':form, 'obj':'user_details:edit-email'})

def profile(request):
    return render(request, 'user_details/profile.html', {})

def edit_password(request):
    if request.method == 'POST':
        user_id = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = request.POST.get('old_password', '')
            new_pass = request.POST.get('password1', '')
            user = auth.authenticate(username=user_id.username, password=password)
            if user is not None:
                auth.login(request, user)
                user.set_password(new_pass)
                user.save()
                response = redirect('user_details:account')
                return response
            else:
                response = redirect('user_details:register')
                return response
        else:
            return render(request, 'user_details/edit_password.html', {'form':form, 'obj':'user_details:edit-password'})
    form = ChangePasswordForm()
    return render(request, 'user_details/edit_password.html', {'form':form, 'obj':'user_details:edit-password'})

def reset_password(request):
    return render(request, 'user_details/reset_password.html', {})

def switch_marketing(request):
    return render(request, 'user_details/edit_marketing.html', {})

def edit_name(request):
    if request.method == 'POST':
        user_id = request.user
        form = ChangeNameForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password', '')
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            user = auth.authenticate(username=user_id.username, password=password)
            if user is not None:
                auth.login(request, user)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                response = redirect('user_details:account')
                return response
            else:
                response = redirect('user_details:register')
                return response
        else:
            return render(request, 'user_details/edit_name.html', {'form':form, 'obj':'user_details:edit-name'})
    form = ChangeNameForm()
    return render(request, 'user_details/edit_name.html', {'form':form, 'obj':'user_details:edit-name'})

def switch_account_status(request):
    return render(request, 'user_details/edit_account.html', {})
