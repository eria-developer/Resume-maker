from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("resume.urls")),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]
