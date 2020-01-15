from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from products.views import *
from . import views

urlpatterns = [

    url(r'^product', views.product,name="product"),   
    url(r'^edit-product/(?P<id>\d+)', views.edit_product,name="edit-product"),  
    url(r'^update-product/(?P<id>\d+)', views.update_product,name="edit-product"),  
    url(r'^delete-product/(?P<id>\d+)', views.delete_product,name="edit-product"),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)