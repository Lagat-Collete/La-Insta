from django.shortcuts import render
from .models import *
from .forms import  Sign_UpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  
  return render(request, 'index.html',locals())

def signup(request):
  if request.method == 'POST':
     form = Sign_UpForm(request.POST)
     if form.is_valid():
       email = form.cleaned_data['email']
       recipient = SignUpRecipients(email=email)
       recipient.save()
       send_welcome_email(email)
       HttpResponseRedirect('signup')
       

  else:
    form = Sign_UpForm()
    return render(request, 'index.html',{'Sign_UpForm':Sign_UpForm})