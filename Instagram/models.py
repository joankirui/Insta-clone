from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    prof_image = CloudinaryField('image',null=True)
    bio = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update_profile()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        user_images = Profile.objects.filter(user=id).first()
        return user_images


class Image(models.Model):
    image = CloudinaryField('image',null=True)
    img_name = models.CharField(max_length=30)
    img_caption = models.TextField()
    img_likes = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='image')

    def __str__(self):
        return self.img_caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def update_caption(self, caption):
        self.img_caption = caption
        self.save()

    class Meta:
        ordering = ['-post_date']

    @classmethod
    def get_image(request, id):
        try:
            image = Image.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return image

    @classmethod
    def get_user(cls, search_term):
        image = cls.objects.filter(user__username__icontains=search_term)
        return image

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_profile_images(cls, profile):
        user_images = Image.objects.filter(profile__id=profile)
        return user_images

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='1')
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_comment(self):
        self.save()

    @classmethod
    def get_all_comments(cls):
        comments = Comment.objects.all()
        return comments

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.user