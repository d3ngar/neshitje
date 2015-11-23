from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Listing, ListingImage


class ListingMainForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('listing_name', 'supplier_id', 'listing_description', 'price', 'keywords', 'condition', 'currency_code')

    def save(self, u, commit=True):
        model = Listing(product_name = self.cleaned_data['listing_name'], supplier_id = self.cleaned_data['supplier_id'], listing_description = self.cleaned_data['listing_description'], price = self.cleaned_data['price'], keywords = self.cleaned_data['keywords'], condition = self.cleaned_data['condition'], currency_code = self.cleaned_data['currency_code'], user=u)

        if commit:
            model.save()
        return model


class ListingImageForm(forms.ModelForm):
    #product = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = ListingImage
        fields = ('image',)

    def save(self, prod, user, commit=True):
        p = Listing.objects.get(id=prod)
        pi = ListingImage(listing=p, image=self.cleaned_data['image'], user=user)

        if commit:
            pi.save()
        return pi
