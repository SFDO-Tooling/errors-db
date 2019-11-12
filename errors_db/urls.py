"""errors-db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from urllib.parse import urljoin

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

PREFIX = settings.ADMIN_AREA_PREFIX


urlpatterns = [
    path(urljoin(PREFIX, r"django-rq/"), include("django_rq.urls")),
    path(
        urljoin(PREFIX, r"rest/"),
        include("errors_db.adminapi.urls", namespace="admin_rest"),
    ),
    # Put this after all other things using `PREFIX`:
    re_path(PREFIX + "$", RedirectView.as_view(url=f"/{PREFIX}/")),
    path(PREFIX + "/", admin.site.urls),
    # path("accounts/", include("allauth.urls")),
    path("", include("errors_db.api.urls")),
]
