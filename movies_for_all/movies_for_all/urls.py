from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('app_user.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
