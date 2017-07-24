from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('otcore.api_urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
