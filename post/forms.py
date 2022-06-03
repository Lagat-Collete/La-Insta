import email
from django import forms

class Sign_UpForm(forms.Form):
  email = forms.EmailField(label='Email')