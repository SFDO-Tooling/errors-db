from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from model_utils import Choices

from . import model_mixins as mixins


class UserManager(BaseUserManager):
    pass


class User(mixins.HashIdMixin, AbstractUser):
    objects = UserManager()

