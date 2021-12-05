from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Instagram.models import Image,Comment,Likes,Profile


# Create your views here.
# @login_required(login_url='/accounts/login')
def index(request):
    title = 'insta-clone'
    return render(request,'index.html',{"title":title})





def search_by_username(request):
    if 'user' in request.GET and request.GET['user']:
        search_term = request.GET['user']
        searched_images = Image.get_user(search_term)
        message = f'{search_term}'
        user = User.objects.all()
        args = {
            "user": user,
            "images": searched_images,
            "message": message
        }
        return render(request, 'search.html', args)
    else:
        message = "search for a user"
        args = {
            "message": message
        }
        return render(request, 'search.html', args)
