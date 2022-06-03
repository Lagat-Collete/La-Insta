from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
import datetime as dt
from django.utils.text import slugify
from cloudinary.models import CloudinaryField 


# Create your models here.

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    profile = models.ForeignKey(User)
    Comments = models.TextField()  
    likes = models.ManyToManyField(User,)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_


 

