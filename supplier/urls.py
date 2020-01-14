from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from supplier.views import *


urlpatterns = [
   url(r'^supplier/$', all_suppliers, name='all_suppliers'),
   url(r'^supplier/add_supplier/$',add_supplier, name='add_supplier'),
   url(r'^supplier/delete_supplier/$',delete_supplier, name='delete_supplier'),
   url(r'^supplier/edit_supplier/$',edit_supplier, name='edit_supplier'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)