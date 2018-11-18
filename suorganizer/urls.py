from django.conf.urls import include, url
from django.contrib import admin
from organizer.views import homepage

urlpatterns = [
    url(r"ˆadmin/", include(admin.site.urls)),
    url(r"ˆ$", homepage),
]
