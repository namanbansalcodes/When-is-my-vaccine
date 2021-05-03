from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    pin = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
