from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from client.views import *
from login.views import *
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^store/',views.shome,name='shome'),
    url(r'^accounting/',views.achome,name='achome'),
    url(r'^administrator/',views.ahome,name='shome'),
    url(r'^users/$', views.users_form,name="add_user"), 
    url(r'^users/(?P<id>\d+)/$', views.users_form,name="update_user"),
    url(r'^users/delete/(?P<id>\d+)/$', views.delete_user,name="delete_user"),
    url(r'^users/list/$',views.users_list,name="users_list"),
    url(r'^main/',views.main,name='main'),
    

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)