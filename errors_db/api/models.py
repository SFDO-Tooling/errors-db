from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from model_utils import Choices

from . import model_mixins as mixins


class UserManager(BaseUserManager):
    pass


class User(mixins.HashIdMixin, AbstractUser):
    objects = UserManager()


class ErrorInstance(models.Model):
    context = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    stacktrace = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["created"]


class Situation(models.Model):
    error_msg = models.TextField()
    context = JSONField()
    created = models.DateTimeField(auto_now_add=True)


class Solution(models.Model):
    UNKNOWN = 0
    RETRY = 1
    CONTENT = 2
    AUTOMATION = 3
    SOLUTION_TYPES = [
        (UNKNOWN, "Unknown"),
        (RETRY, "Retry"),
        (CONTENT, "Content"),
        (AUTOMATION, "Automation"),
    ]
    solution_type = models.PositiveIntegerField(choices=SOLUTION_TYPES, default=UNKNOWN)
    text = models.TextField()
    situation = models.ForeignKey(Situation, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
