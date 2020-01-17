from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from .views import *

urlpatterns = [

    url(r'^material/$',all_materials,name='all_materials'),
    url(r'^material/add_material/$',add_material, name='add_material'),
    url(r'^material/delete_material/(?P<pk>\d+)$',delete_material, name='delete_material'),
    url(r'^material/edit_material/(?P<pk>\d+)$',edit_material, name='edit_material'),
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)