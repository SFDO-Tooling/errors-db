from .base import *  # NOQA
from .base import LOGGING

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]  # NOQA

LOGGING["loggers"]["werkzeug"] = {
    "handlers": ["console"],
    "level": "DEBUG",
    "propagate": True,
}

# Don't use HTTPS
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
