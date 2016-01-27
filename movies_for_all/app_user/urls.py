from django.conf.urls import patterns, include, url

from .views import CreateAppUser

urlpatterns = [
    url(r'^$', CreateAppUser.as_view(), name="user_list"),
]
