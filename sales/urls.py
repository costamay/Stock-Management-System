from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from .views import *


urlpatterns = [
   url(r'^sales_report/$', sales_report, name='sales_report'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)