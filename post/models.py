from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
import datetime as dt
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profile_photo = models.CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    profile = models.ForeignKey(User)
    Comments = models.TextField()  
    likes = models.ManyToManyField(User,)
    pup_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['reverse']    

   
    def __str__(self):
       return self.name


class Comment(models.Model):
    comment = models.TextField(max_length=500)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

 

