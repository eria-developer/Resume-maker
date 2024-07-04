from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/app/", include("resume.urls")),
    path("api/v1/auth/", include("authentication.urls")),
]
