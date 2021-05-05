from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    email = forms.CharField(required=True, strip=True, 
                            widget=forms.TextInput(attrs={'class': 'form-control'}), label='Email',
                            label_suffix=''
                            )

    pin = forms.IntegerField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix=''
                             )
