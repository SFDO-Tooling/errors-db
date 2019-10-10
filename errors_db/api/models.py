from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from model_utils import Choices

from enum import Enum

from . import model_mixins as mixins


class UserManager(BaseUserManager):
    pass


class User(mixins.HashIdMixin, AbstractUser):
    objects = UserManager()


class ErrorMessage(models.Model):
    message = models.TextField()


class ErrorInstance(models.Model):
    context = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(ErrorMessage, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]

