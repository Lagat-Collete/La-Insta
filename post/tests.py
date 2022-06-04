from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
  def setUp(self):
    self.user = User(username = 'lagat')
    self.user.save()
    self.profile_test = Profile(id=1, name='image', profile_photo='test.png', bio='just testing functionality',
        user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test,Profile))
    
    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)    

class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='collete', user=User(username='lagat'))
        self.profile_test.save()

        self.image_test = Image(user=self.profile_test,image='test.png', name='testing', caption='Just Testing',)
    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        post = Profile.objects.all()
        self.assertTrue(len(post) == 0)
    
    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()    