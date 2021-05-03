from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    phone = forms.PhoneNumberField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    pin = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
