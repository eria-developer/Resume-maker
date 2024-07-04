from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _ 
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken


AUTH_PROVIDERS = {
    "email": "email",
    "google": "google",
    "github": "github",
    "facebook": "facebook"
}
class CustomUser(AbstractBaseUser, PermissionsMixin):
     # Add related_name to the groups field
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    # Add related_name to the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    email = models.EmailField(max_length=254, unique=True, verbose_name=_("Email Address"))
    first_name = models.CharField(max_length=254, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=254, verbose_name=_("Last Name"))
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(max_length=254, default=AUTH_PROVIDERS.get("email"))

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
    
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def user_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


class OneTimePassword(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.user.first_name}-passcode"