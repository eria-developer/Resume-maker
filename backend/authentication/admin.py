from django.contrib import admin
from .models import CustomUser, OneTimePassword


admin.site.register(CustomUser)
admin.site.register(OneTimePassword)