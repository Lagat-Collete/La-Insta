from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name='home_page'),
    path('index/', views.index, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('post/', views.post, name='post'),
    path('userprofile/<username>', views.user_profile, name='user_profile'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit_profile'),
    path('post/<int:post_id>/like', views.like_post, name='like'),
    path('signout/', views.signout, name='signout'),
    path('search/', views.search_profile, name='search'),
    path('', include('django.contrib.auth.urls')),
]


# urlpatterns = [
#   path('admin/', admin.site.urls),
#   # path('',views.home_page, name='home_page'),
#   path('',views.index, name = 'home'),
#   path('comment/<int:id>/', views.comment_image, name ='comment_image'),
#   path('image/<int:id>/like', views.like, name='like'),
#   path('', include('django.contrib.auth.urls')),
#   path('search/', views.search_profile, name='search'),
#   path('profile/<username>/',views.profile, name='profile'),
#   path('userprofile/<username>/', views.user_profile, name='userprofile'),
# ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
