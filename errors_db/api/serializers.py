from errors_db.api.models import ErrorInstance
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class FullUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "is_staff")


class ErrorInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorInstance
        fields = "__all__"
