from django.conf.urls import url
from .views import get_photosets, photoset_detail, create_or_edit_photoset


urlpatterns = [
    url(r'^$', get_photosets, name='shop'),
    url(r'^(?P<pk>\d+)/$', photoset_detail, name='photoset_detail'),
    url(r'^new/$', create_or_edit_photoset, name='new_photoset'),
    url(r'^(?P<pk>\d+)/$', create_or_edit_photoset, name='edit_photoset'),
]
