from django.shortcuts import render

# Create your views here.
def index(request):
  title = 'home page'
  return render(request, 'index.html',locals())