from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof_image = CloudinaryField('image',null=True)
    bio = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update_profile()

    def delete_profile(self):
        self.delete()
