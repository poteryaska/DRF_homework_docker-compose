from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from studying.models import NULLABLE

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=40, verbose_name='number phone', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []