from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserView
from errors_db.api.views import ErrorInstanceViewSet


#
# URL Configuration
#
router = DefaultRouter()
router.register(r"error", ErrorInstanceViewSet)
urlpatterns = router.urls
