from django.conf.urls import url

from gallery.views import *

app_name = 'accounts'

urlpatterns = [
    url(r'^$', GalleryList.as_view(), name='list'),
]