from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import  *
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

@login_required(login_url='/accounts/login/')
def comment_image(request,id):
    template_name = 'comments.html'
    image = get_object_or_404(Image, pk=id)
    comments = image.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
       comment_form = CommentForm(data=request.POST)
       if comment_form.is_valid():
         new_comment = comment_form.save(commit=False)
         new_comment.image = image
         new_comment.save()

    else:
        comment_form = CommentForm()
    return render (request, template_name, {'image':image, 'comments':comments,'comment_form':comment_form})
    

 
