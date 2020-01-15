from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
   url('^orders/$', views.orders),
   url('^create/$', views.create_orders),
   url('^update/$',views.update_orders),
   url(r'delete_orders/(?P<pk>\d+)$',views.delete_orders, name='delete_orders'),
   url('^search_orders/$',views.search_orders),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)