from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof_image = CloudinaryField('image',null=True)
    bio = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update_profile()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = CloudinaryField('image',null=True)
    img_name = models.CharField(max_length=30)
    img_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)