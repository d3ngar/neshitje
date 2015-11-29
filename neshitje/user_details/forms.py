from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetail, UserBilling, UserShipping
from .validators import validate_email_unique
from django.core.mail import EmailMultiAlternatives

class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label="Firstname")
    last_name =  forms.CharField(label="Lastname")
    email = forms.CharField(label="Email", validators=[validate_email_unique])
    phone =  forms.RegexField(regex=r'^\+?\d{6,15}$', error_message = ("Phone number must be entered. Can start '+', but can have no spaces. Six required and up to 15 digits allowed."))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            detail = UserDetail(user_id=user.id)
            detail.phone_number = self.cleaned_data['phone']
            detail.save()

        self.send_welcome_email()

        return user

    def send_welcome_email(self):
        subject, from_email, to = 'Welcome to Neshitje', 'info@neshitje.com', self.cleaned_data['email']
        text_content = """
            Hello """ + self.cleaned_data['first_name'] + """,

            We have created an account for www.neshitje.com for your email address.
            Your username is """ + self.cleaned_data['username'] + """.

            You are now free to post and send and receive messages.

            - The Ne Shitje team
        """
        html_content = """
            <p>Hello """ + self.cleaned_data['first_name'] + """,</p>

            <p>We have created an account for <a href="www.neshitje.com" title="Ne Shitje">Ne Shitje</a> for your email address.
            Your username is: <strong>""" + self.cleaned_data['username'] + """</strong>.</p>

            <p>You are now free to post and send and receive messages.</p>

            <p>- The Ne Shitje team</p>
        """
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


class BillingForm(forms.ModelForm):
    class Meta:
        model = UserBilling
        fields = ['address_line_1', 'address_line_2', 'address_line_3', 'city', 'post_code']

    def save(self, u, commit=True):
        model = UserBilling(address_line_1 = self.cleaned_data['address_line_1'], address_line_2 = self.cleaned_data['address_line_2'], address_line_3 = self.cleaned_data['address_line_3'], city = self.cleaned_data['city'], post_code = self.cleaned_data['post_code'], user = u)

        if commit:
            model.save()
        return model


class PostalForm(forms.ModelForm):
    class Meta:
        model = UserShipping
        fields = ['address_nick', 'address_line_1', 'address_line_2', 'address_line_3', 'city', 'post_code']

    def save(self, u, commit=True):
        model = UserShipping(address_line_1 = self.cleaned_data['address_line_1'], address_line_2 = self.cleaned_data['address_line_2'], address_line_3 = self.cleaned_data['address_line_3'], city = self.cleaned_data['city'], post_code = self.cleaned_data['post_code'], user = u, address_nick = self.cleaned_data['address_nick'])

        if commit:
            model.save()
        return model

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput())


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label="Email", validators=[validate_email_unique])
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label="New password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm", widget=forms.PasswordInput())
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password2 and password1 and password2 != password1:
            self._errors['password1'] = self.error_class(['Passwords do not match.'])
            del self.cleaned_data['password1']
            del self.cleaned_data['password2']
        return cleaned_data

class ChangeNameForm(forms.Form):
    firstname = forms.CharField(label="Firstname")
    lastname = forms.CharField(label="Lastname")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class CloseAccountForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class ChangeEmailOptinForm(forms.Form):
    optin = forms.BooleanField()

class ChangePhoneForm(forms.Form):
    phone =  forms.RegexField(regex=r'^\+?\d{6,15}$', error_message = ("Phone number must be entered. Can start '+', but can have no spaces. Six required and up to 15 digits allowed."))
