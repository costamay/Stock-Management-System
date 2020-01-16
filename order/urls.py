from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
   url('^orders/$', views.orders, name='orders'),
   url('^create_orders/$', views.create_orders, name='create_orders'),
   url(r'^update_orders/(?P<pk>\d+)$',views.update_orders, name='update_orders'),
   url(r'^delete_orders/(?P<pk>\d+)$',views.delete_orders, name='delete_orders'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)