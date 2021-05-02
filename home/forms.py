from django import forms
from .models import User



class UserForm(forms.Form):
    phone = forms.IntegerField(label='Phone', required=True)
    pin = forms.IntegerField(label='Pin', required=True)
