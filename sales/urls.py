from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from .views import *


urlpatterns = [
   url(r'^sales_report/$', sales_report, name='sales_report'),
   url(r'^sales/add_sell/$', add_sell, name='add_sell'),
   url(r'^sales/$', sales, name='sales'),
   url(r'^export_salesreport/$', export_salesreport_to_xlsx, name='exportsales'),
   url(r'^filter/$', filter, name='filter'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)