from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile,Image

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='joan')
        self.user.save()

        self.profile_test = Profile(id=1,prof_image = 'default.jpg', bio='this is a test profile',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test,Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        later = Profile.objects.all()
        self.assertTrue(len(later) > 0)

class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='joan', user=User(username='lala'))
        self.profile_test.save()

        self.image_test = Image(image='default.png', img_name='test', img_caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.asserTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        later = Profile.objects.all()
        self.assertTrue(len(later) < 1)
        

