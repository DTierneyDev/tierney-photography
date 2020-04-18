from django.conf.urls import url
from .views import login, logout, registration, user_profile


urlpatterns = [
    # url(r'^$', index, name='index'),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
]
