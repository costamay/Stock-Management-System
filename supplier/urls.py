from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import  static

from . views import *

urlpatterns = [
  
   url(r'^supplier/$', all_suppliers, name='all_suppliers'),
   url(r'^supplier/add_supplier/$',add_supplier, name='add_supplier'),
   url(r'^supplier/delete_supplier/(?P<pk>\d+)$',delete_supplier, name='delete_supplier'),
   url(r'^supplier/edit_supplier/(?P<pk>\d+)/$',edit_supplier, name='edit_supplier'),
   url(r'^purchase_report/$', purchase_report, name='purchase_report'),
   url(r'^todays_purchase/$', todays_purchase, name='todays_purchase'),
   url(r'^export_purchasesreport/$', export_purchasesreport_to_xlsx, name='export'),
   url(r'^filter_purchase/$', filter_purchase, name='filter_purchase'),
   url(r'^suppliers/search/', search_suppliers, name='search_suppliers'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

