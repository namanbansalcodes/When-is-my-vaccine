from django import forms
from .models import Customer
from phone_field import PhoneField

class CustomerForm(forms.Form):
    phone = PhoneField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    pin = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
