from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.dispatch import receiver
import datetime as dt
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    name = models.CharField(blank=True, max_length=50)
    profile_photo = CloudinaryField('photo')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def search_profile(cls,name):
        profiles = cls.objects.filter(user__username__icontains=name).all()
        return profiles
   
    def __str__(self):
        return f'{self.user.username} Profile'



class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField()  
    pup_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True,)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term).all()
        return images
   
    def __str__(self):
       return self.name


class Comments(models.Model):
    comment = models.TextField(max_length=500)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment')
    posted_on = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def display_by_id(cls, image_id):
        comments = cls.objects.filter(image=image_id)
        return comments

   
    def __str__(self):
       return self.comment

class SignUpRecipients(models.Model):
    email = models.EmailField()

class likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_likes')
    
    def __str__(self):
        return self.image
 

