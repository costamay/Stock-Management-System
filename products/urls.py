from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from products.views import *
from . import views


urlpatterns = [
    
    url(r'^products/$', views.product_form,name="add_product"), 
    url(r'^products/(?P<id>\d+)/$', views.product_form,name="update_product"),
    url(r'^products/delete/(?P<id>\d+)/$', views.delete_product,name="delete_product"),
    url(r'^products/list/$',views.product_list,name="product_list"),
    url(r'^products/search/', views.search_products, name='search_products'),
    url(r'^products/reorder_notification/', views.reorder_notification, name='reorder_notification'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)