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
    

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)