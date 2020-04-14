from django.conf.urls import url
from .views import index, login, logout, registration, user_profile


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', user_profile, name="profile"),
]
