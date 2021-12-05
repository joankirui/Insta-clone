from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url('search/',views.search_by_username,name='search_by_username'),
    url('profile/',views.profile,name='profile'),
    url('post/', views.post_pic,name='post_pic')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)