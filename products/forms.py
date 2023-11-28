from django import forms
from .models import Product

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'description', 'image']


class CheckoutForm(forms.Form):
    c_fname = forms.CharField(label='First Name', max_length=100, required=True)
    c_lname = forms.CharField(label='Last Name', max_length=100, required=True)
    c_address = forms.CharField(label='Address', max_length=255, required=True)
    c_address_optional = forms.CharField(label='Apartment, suite, unit etc. (optional)', max_length=255, required=False)
    c_email_address = forms.EmailField(label='Email Address', required=True)
    c_phone = forms.CharField(label='Phone', max_length=20, required=True)
    c_order_notes = forms.CharField(label='Order Notes', widget=forms.Textarea(attrs={'rows': 5}), required=False)


class CartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, initial=1)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Add to Cart'))