from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from sales.views import *


urlpatterns = [
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)