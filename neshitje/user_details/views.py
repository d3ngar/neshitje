from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth, messages
from django.core.context_processors import csrf
from .forms import UserRegForm, BillingForm, PostalForm, LoginForm, ChangeEmailForm, ChangePasswordForm, ChangeNameForm, CloseAccountForm, ChangeEmailOptinForm, ChangePhoneForm
from .models import UserBilling, UserShipping
from main_app.models import Status

import main_app.recaptcha_simple

### Universal functions ###

### Captcha Section, leave only one of them. If former, you don't need to install recaptcha-client ###

### From here on is views: ###
def add_billing(request):
    if request.user.is_authenticated():
        user_id = request.user

        if request.method == 'POST':
            form = BillingForm(request.POST)
            if form.is_valid():
                try:
                    billing = UserBilling.objects.get(user_id=user_id, status=1)
                    if billing is not None:
                        billing.status = Status.objects.get(pk=3)
                        billing.save()

                except:
                    print "this is the first billing address"

                form.save(user_id)

                if request.POST.get('save') == 'submit':
                    messages.success(request, "Billing address created!")
                    response = redirect('user_details:account')

                elif request.POST.get('add_shipping') == 'submit':
                    messages.success(request, "Billing address created!")
                    response = redirect('user_details:add-shipping')

                else:
                    response = redirect('user_details:account')

                return response

            else:
                messages.warning(request, "Your billing address couldn't be updated")
                form = BillingForm(instance=billing)
                return render(request, 'user_details/add_billing_address.html', {'form' : form})

        else:
            billing = None
            try:
                billing = UserBilling.objects.get(user_id=user_id, status=1)
            except:
                #messages.info(request, "This would be your first billing address")
                print "this is the first billing address"

            form = BillingForm(instance=billing)
            return render(request, 'user_details/add_billing_address.html', {'form': form})

    else:
        request.session['direct_url'] = 'user_details:add-billing'
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
                messages.success(request, "Postal address added!")
                response = redirect('user_details:account')
                return response

            return render(request, 'user_details/add_postal_address.html', {'form' : form, 'postals':postals})
        else:
            form = PostalForm()
            return render(request, 'user_details/add_postal_address.html', {'form': form, 'postals':postals})

    else:
        request.session['direct_url'] = 'user_details:add-postal'
        response = redirect('user_details:logging')
        return response


def logging(request):

    if not request.session.get('direct_url', False):
        messages.warning(request, "We are sorry, we forgot where you want to go, so we sent you here.")
        url = "user_details:register"
    else:
        url = request.session.get('direct_url')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Thank you for logging in")
                response = redirect(url)
                return response
            else:
                messages.warning(request, "There was an error logging you in.")
                response = redirect('user_details:logging')
                return response
        else:
            messages.warning(request, "There was an error trying to log you in")
            return render(request, 'user_details/logging.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'user_details/logging.html', {'form': form})


def login_process(request):

    referrer = None
    try:
        referrer = request.META['HTTP_REFERER']
    except KeyError:
        referrer = "user_details:register"

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        messages.success(request, "Hello " + user.first_name + ", you are now logged in.")
        response = redirect(referrer)
        return response
    else:
        response = redirect(referrer)
        messages.error(request, "User not found!")
        return response


def logout_process(request):

    referrer = None
    try:
        referrer = request.META['HTTP_REFERER']
    except KeyError:
        referrer = 'main_app:homepage'

    if request.session.get('delete'):
        delete = request.session.get('delete')
        user = request.user
        if user.id == delete:
            user.is_active = False
            user.userdetail.status_id = 3
            user.userdetail.save()
            user.save()
            messages.success(request, "Your account was successfully deactivated.")
    auth.logout(request)
    messages.success(request, "Logged out!")
    return redirect(referrer)


def register(request):
    if request.method == 'POST':
        #print request
        response = main_app.recaptcha_simple.submit(request.POST.get('g-recaptcha-response'), request.META['REMOTE_ADDR'])
        if response.is_valid:
            form = UserRegForm(request.POST)
            if form.is_valid():
                print "User reg form success"
                form.save()
                messages.success(request, "Account created!")
                if request.POST.get('details') == 'submit':
                    response = redirect('user_details:add-billing')
                else:
                    response = redirect('user_details:account')
                return response
            else:
                return render(request, 'user_details/register_base.html', {'form' : form})
        else:
            # return the form
            messages.warning(request, "The re-captcha was most likely wrong!")
            response = redirect('user_details:register')
            response['Location'] += '?fail=recaptcha'
            return response

    form = UserRegForm()
    return render(request, 'user_details/register_base.html', {'form' : form})

def delete_postal(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            postal_id = request.GET.get('postal_id', None)
            post_add = UserShipping.objects.get(id=postal_id)
            post_add.status = 3
            post_add.save();
            messages.success(request, "Postal address deleted!")
        return render(request, 'user_details/account.html', {})
    else:
        request.session['direct_url'] = 'user_details:del-postal'
        response = redirect('user_details:logging')
        return response

def account(request):
    if request.user.is_authenticated():
        return render(request, 'user_details/account.html', {})
    else:
        request.session['direct_url'] = 'user_details:account'
        response = redirect('user_details:logging')
        return response


## This one is mainly to try around in.
def edit_phone(request):
    if request.user.is_authenticated():

        if request.method == 'POST':
            form = UserRegForm(request.POST)
            if form.is_valid():
                print "User reg form success"
                form.save()
                messages.success(request, "Phone number updated.")
                response = redirect('user_details:account')
                return response
            else:
                messages.warning(request, "Phone number not updated.")
                return render(request, 'user_details/edit_phone.html', {'form' : form})
        return render(request, 'user_details/edit_phone.html', {'form' : form})

    else:
        request.session['direct_url'] = 'user_details:edit-phone'
        response = redirect('user_details:logging')
        return response

def edit_email(request):
    if request.user.is_authenticated():
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
                    messages.success(request, "Email address updated")
                    response = redirect('user_details:account')
                    return response
                else:
                    messages.warning(request, "Email address not updated")
                    response = redirect('user_details:edit-email')
                    return response
            else:
                messages.warning(request, "Email address not updated")
                return render(request, 'user_details/edit_email.html', {'form':form, 'obj':'user_details:edit-email'})
        form = ChangeEmailForm()
        return render(request, 'user_details/edit_email.html', {'form':form, 'obj':'user_details:edit-email'})

    else:
        request.session['direct_url'] = 'user_details:edit-email'
        response = redirect('user_details:logging')
        return response

def profile(request):
    if request.user.is_authenticated():
        return render(request, 'user_details/profile.html', {})
    else:
        request.session['direct_url'] = 'user_details:profile'
        response = redirect('user_details:logging')
        return response

def edit_password(request):
    if request.user.is_authenticated():

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
                    messages.success(request, "Your password has been updated")
                    response = redirect('user_details:account')
                    return response
                else:
                    messages.warning(request, "Your password was not updated")
                    response = redirect('user_details:edit-password')
                    return response
            else:
                messages.warning(request, "Your password was not updated")
                return render(request, 'user_details/edit_password.html', {'form':form, 'obj':'user_details:edit-password'})
        form = ChangePasswordForm()
        return render(request, 'user_details/edit_password.html', {'form':form, 'obj':'user_details:edit-password'})

    else:
        request.session['direct_url'] = 'user_details:edit-password'
        response = redirect('user_details:logging')
        return response

def reset_password(request):
    return render(request, 'user_details/reset_password.html', {})

def switch_marketing(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            optin = request.POST.get('optin', '')
            request.user.userdetail.marketing_optin = optin
            request.user.userdetail.save()
            messages.success(request, "Marketing preferences updated.")
        optin = request.user.userdetail.marketing_optin
        form = ChangeEmailOptinForm()
        return render(request, 'user_details/edit_marketing.html', {'form':form, 'optin':optin})
    else:
        request.session['direct_url'] = 'user_details:edit-marketing'
        return redirect('user_details:logging')

def edit_name(request):
    if request.user.is_authenticated():

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
                    messages.success(request, "Your name has been updated successfully")
                    response = redirect('user_details:account')
                    return response
                else:
                    messages.warning(request, "Your name couldn't be updated")
                    response = redirect('user_details:register')
                    return response
            else:
                messages.warning(request, "Your name couldn't be updated")
                return render(request, 'user_details/edit_name.html', {'form':form, 'obj':'user_details:edit-name'})
        form = ChangeNameForm()
        return render(request, 'user_details/edit_name.html', {'form':form, 'obj':'user_details:edit-name'})

    else:
        request.session['direct_url'] = 'user_details:edit-name'
        response = redirect('user_details:logging')
        return response

def switch_account_status(request):
    if request.user.is_authenticated():
        user_id = request.user
        form = CloseAccountForm()
        if request.method == 'POST':
            form = CloseAccountForm(request.POST)
            if form.is_valid:
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                user = auth.authenticate(username=username, password=password)

                if user is not None and user == user_id:
                    request.session['delete'] = user_id.id
                    response = redirect('user_details:logout')
                    return response
                else:
                    response = redirect('user_details:register')
                    return response

        return render(request, 'user_details/edit_account.html', {'form':form, 'user':user_id})

    else:
        request.session['direct_url'] = 'user_details:status-switch'
        return redirect('user_details:logging')

def edit_phone(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            user_id = request.user
            form = ChangePhoneForm(request.POST)
            if form.is_valid():
                phone = request.POST.get('phone', '')
                user_id.userdetail.phone_number = phone
                print user_id.userdetail.phone_number
                user_id.userdetail.save()
                messages.success(request, "Your phone number has been udpated.")
                response = redirect('user_details:account')
                return response
            else:
                messages.warning(request, "Your phone number could not be updated.")
                return render(request, 'user_details/edit_phone.html', {'form':form, 'obj':'user_details:edit-phone'})
        else:
            form = ChangePhoneForm()
            return render(request, 'user_details/edit_phone.html', {'form':form, 'obj':'user_details:edit-phone'})

    else:
        request.session['direct_url'] = 'user_details:edit-phone'
        response = redirect('user_details:logging')
        return response
