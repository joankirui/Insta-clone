from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/',views.search_by_username,name='search_by_username'),
    path('profile/',views.profile,name='profile'),
    path('post/', views.post_pic,name='post_pic')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)