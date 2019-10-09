import factory
import pytest
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib.auth import get_user_model
from pytest_factoryboy import register
from rest_framework.test import APIClient

User = get_user_model()


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence("user_{}@example.com".format)
    username = factory.Sequence("user_{}@example.com".format)
    password = factory.PostGenerationMethodCall("set_password", "foobar")


@pytest.fixture
def client(user_factory):
    user = user_factory()
    client = APIClient()
    client.force_login(user)
    client.user = user
    return client


# @pytest.fixture
# def admin_api_client(user_factory):
#     user = user_factory(is_superuser=True)
#     client = APIClient()
#     client.force_login(user)
#     client.user = user
#     return client


# @pytest.fixture
# def anon_client():
#     return APIClient()
