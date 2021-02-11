from django.conf.urls import url

from gallery.views import *

app_name = 'gallery'

urlpatterns = [
    url(r'^$', GalleryList.as_view(), name='list'),
    url(r'^new/$', GalleryCreate.as_view(), name='new'),
    url(r'^detail/(?P<pk>\d+)/$', GalleryDetail.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', GalleryUpdate.as_view(), name='update'),
]
