from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login')
def index(request):
    title = 'insta-clone'
    return render(request,'index.html',{"title":title})

