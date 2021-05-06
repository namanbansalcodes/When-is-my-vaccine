from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    email = forms.CharField(required=True, strip=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}), label='Email',
                            label_suffix=''
                            )

    phone = forms.CharField(required=True, strip=True, max_length=10,
                            widget=forms.TextInput(attrs={'class': 'form-control'}), label='Phone Number',
                            label_suffix=''
                            )

    pin = forms.CharField(required=True, max_length=69,
                          widget=forms.TextInput(attrs={'class': 'form-control'}), label='Pincodes (seperated by space)', 
                          label_suffix='')
