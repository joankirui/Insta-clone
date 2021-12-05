from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Instagram.forms import CommentForm, EditProfileForm, PostPicForm, ProfileUpdateForm, RegisterForm
from Instagram.models import Image,Comment,Likes,Profile


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form": form})

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
            comment = form.save(commit=False)
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

# @login_required(login_url='/login')
def post_pic(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostPicForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')
    else:
        form = PostPicForm(auto_id=False)
    return render(request, 'new_pic.html', {"form": form})

@login_required(login_url='/login')
def profile(request):
    pics = Image.get_images()
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
    return render(request, 'profile.html', {"u_form": u_form, "p_form": p_form, "pics": pics})



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
