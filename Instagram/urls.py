from django.conf.urls import url,include
from . import views
from django.urls import path
from django_registration.backends.one_step.views import RegistrationView

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('search/',views.search_by_username,name='search_by_username'),
    path('profile/',views.profile,name='profile'),
    path('post/', views.post_pic,name='post_pic')
    
]
