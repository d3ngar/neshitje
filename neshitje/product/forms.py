from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Product, ProductImage


class ProductMainForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'supplier_id', 'product_description', 'price', 'keywords', 'condition', 'currency_code')

    def save(self, u, commit=True):
        model = Product(product_name = self.cleaned_data['product_name'], supplier_id = self.cleaned_data['supplier_id'], product_description = self.cleaned_data['product_description'], price = self.cleaned_data['price'], keywords = self.cleaned_data['keywords'], condition = self.cleaned_data['condition'], currency_code = self.cleaned_data['currency_code'], user=u)

        if commit:
            model.save()
        return model


class ProductImageForm(forms.ModelForm):
    #product = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = ProductImage
        fields = ('image',)

    def save(self, prod, user, commit=True):
        p = Product.objects.get(id=prod)
        pi = ProductImage(product=p, image=self.cleaned_data['image'], user=user)

        if commit:
            pi.save()
        return pi
