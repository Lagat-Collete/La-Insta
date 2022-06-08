from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(label='Email')

  class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('profile_photo','bio','user')


class CommentForm(forms.ModelForm):
  comment = forms.CharField()

  class Meta:
    model = Comments
    fields = ['comment']
    widgets = {
            Comment: forms.Textarea(attrs={'rows':1, 'cols':15}),
        }

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['image','caption']