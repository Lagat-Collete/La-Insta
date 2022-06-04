from audioop import reverse
from django.forms import ImageField
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import  *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  images = Image.objects.all()
  print('IMG', images)
  users = User.objects.exclude(id=request.user.id)
  if request.method =='POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user.profile
      post.save()
      return HttpResponseRedirect(request.path_info)
  else:
    form = PostForm()
  index_context = {'images':images,'form': form, 'users':users}

  
  return render(request, 'index.html',index_context)

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



def like(request, image_id):
  user = request.user
  image = Image.objects.get(id=image_id)
  current_likes = image.likes
  liked = likes.objects.filter(user=user,image=image).count()
  if not liked:
    liked = likes.objects.create(user=user, image=image)
    current_likes = current_likes + 1
  else:
    liked = likes.objects.filter(user=user,image=image).delete()
    current_likes = current_likes - 1

  image.likes =current_likes
  image.save()
  return HttpResponseRedirect(reverse('',args =[image_id]))


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
 
