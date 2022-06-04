from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image,Comments
from django import forms

class Sign_UpForm(UserCreationForm):
  email = forms.EmailField(label='Email')

  class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('profile_photo','bio','user')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    fields = ('comment')

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ('image','name','caption','comments')