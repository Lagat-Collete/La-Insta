from audioop import reverse
from imaplib import _Authenticator
from django.forms import ImageField
from django.shortcuts import get_object_or_404, redirect, render
import requests
from .models import *
from .forms import  *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth import  authenticate,login,logout

# Create your views here.

def home_page(request):
    return render(request,'home_page.html')




@login_required
def index(request):
    images = Post.objects.all()
    current_user = request.user
    form = CommentForm()
    if request.method =='POST':
        if 'postComment' in request.POST:
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.author = current_user
            comment.save()
            
    
    return render(request, 'index.html', {'images':images, 'form':form})

@login_required
def single_post(request, post_id):
    post =  get_object_or_404(Post,id = post_id)
    comments = Comments.objects.filter(post=post).all()
    current_user = request.user 
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user 
            comment.post = post
            comment.save()
        return redirect('singlepost',post_id=post.id)
    else:
        
        form = CommentForm()
    return render(request, 'singlepost.html', {'post': post, 'form':form, 'comments':comments})


def register(request):
    if request.method == 'POST':
        
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            
            authenticate and login 
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect('home')
            
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})


@login_required
def post(request):
    if request.method == 'POST':
      current_user = request.user
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.user = current_user
          post.save()
      return redirect('home')
          
    else:
        form = PostForm()
        
    return render(request,'post.html', {'form':form})



@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post,id = post_id)
    like = Like.objects.filter(image = post ,user = request.user).first()
    if like is None:
        like = Like()
        like.post = post
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('home')



@login_required
def user_profile(request,username):
    user = User.objects.filter(username=username).first()
    if user == request.user:
        return redirect('profile',username = user.username)
    profile = get_object_or_404(Profile,id = user.id)
    images = Post.objects.filter(author=user)
    return render(request, 'userprofile.html', {'user': user,'profile':profile,'images':images})



@login_required
def profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    images = Post.objects.filter(author=user)
    return render(request, 'profile.html', {'user': user,'images':images})




@login_required
def edit_profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    profile = get_object_or_404(Profile,user=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profileform = form.save(commit=False)
            profileform.user = user
            profileform.save()
        return redirect('profile',username =user.username)
           
    else:
        form = EditProfileForm()
    
    return render(request, 'edit_profile.html', {'form':form, 'user': user})

@login_required(login_url='/accounts/login/')
def search_profile(request):
  if 'search_user' in request.GET and request.GET['search_user']:
  
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        search_context= { 'results': results, 'message': message }
        return render(request, 'search.html', search_context)
  else:
      message = "Please search for a valid username"
  return render(request, 'search.html',{'message': message})
 


def signout(request):
    logout(request)
    return redirect('home')














