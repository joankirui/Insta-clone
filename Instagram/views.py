from django.contrib.auth import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Instagram.forms import CommentForm, EditProfileForm, PostPicForm, ProfileUpdateForm, RegisterForm
from Instagram.models import Image,Comment,Likes,Profile
from cloudinary.models import CloudinaryField
from django import forms

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {"form": form})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def post_pic(request):
    current_user = request.user
    form = PostPicForm()
    if request.method == 'POST':
        form = PostPicForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            # context = {
            #     "current_user": current_user,
            #     "form": PostPicForm
            # }
            
            #image.save()
            # form.instance.user = request.user
            # form.save()
        return redirect('/')
    
       
    return render(request, 'new_pic.html', {"current_user": current_user,"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    pics = Image.get_images()
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
    return render(request, 'profile.html', {"u_form": u_form, "p_form": p_form, "pics": pics})


@login_required(login_url='/accounts/login/')
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
