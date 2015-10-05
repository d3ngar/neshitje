from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetail, UserBilling, UserShipping
from .validators import validate_email_unique

class RegisterBaseForm(forms.Form):
    first_name = forms.CharField(label="Firstname")
    last_name =  forms.CharField(label="Lastname")
    user_name =  forms.CharField(label="Username")
    email = forms.CharField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label="Firstname")
    last_name =  forms.CharField(label="Lastname")
    email = forms.CharField(label="Email", validators=[validate_email_unique])

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
            detail.save()

        return user
