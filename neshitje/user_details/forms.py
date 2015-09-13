from django import forms

class RegisterBaseForm(forms.Form):
    first_name = forms.CharField(label="Firstname", max_length=100)
    last_name =  forms.CharField(label="Lastname", max_length=100)
    user_name =  forms.CharField(label="Username", max_length=100)
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
