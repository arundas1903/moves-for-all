from django.conf.urls import url

from .views import User, UserLogin

urlpatterns = [
    url(r'^$', User.as_view(), name="user_list"),
    url(r'^login_token/$', UserLogin.as_view()),
]
