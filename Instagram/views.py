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
    posts = Image.get_images()
    comments = Comment.get_all_comments()
    users = User.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(ccommit=False)
            comment.user = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}',)
    else:
        form = CommentForm(auto_id=False)

        param = {
            "title": title,
            "posts": posts,
            "form": form,
            "comments": comments,
            "users": users
        }
    return render(request,'index.html',param)





def search_by_username(request):

    if 'user' in request.GET and request.GET['user']:
        search_term = request.GET['user']
        searched_images = Image.get_user(search_term)
        message = f'{search_term}'
        user1 = User.objects.all()
        args = {
            "user1": user1,
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
