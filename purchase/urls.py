from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views


urlpatterns = [
   url('^purchases/$', views.purchases),
   url('^create_purchases/$', views.create_purchases),
   url('^update_purchases/$', views.update_purchases),
   url(r'delete_purchases/(?P<pk>\d+)$',views.delete_purchases),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)