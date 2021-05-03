from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    phone = forms.CharField(required=True, strip=True, max_length=14, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    pin = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
