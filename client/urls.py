from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    url(r'^clients/$', views.client_form,name="add_client"), 
    url(r'^clients/(?P<id>\d+)/$', views.client_form,name="update_client"),
    url(r'^clients/delete/(?P<id>\d+)/$', views.delete_client,name="delete_client"),
    url(r'^clients/list/$',views.client_list,name="client_list"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)