from django.contrib import admin
from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',views.index, name = 'home'),
  path('comment/<int:id>/', views.comment_image, name ='comment_image'),
  path('image/<int:id>/like', views.like, name='like')
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
