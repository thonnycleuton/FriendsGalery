from django.conf.urls import url

from gallery.views import *

app_name = 'gallery'

urlpatterns = [
    url(r'^$', GalleryList.as_view(), name='list'),
    url(r'^new/$', GalleryCreate.as_view(), name='new'),
    url(r'^detail/(?P<pk>\d+)/$', GalleryDetail.as_view(), name='detail'),
    url(r'^new_interaction/$', InteractionCreate.as_view(), name='new_interaction'),
]
