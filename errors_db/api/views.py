from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from .serializers import FullUserSerializer
from errors_db.api.models import ErrorInstance
from errors_db.api.serializers import ErrorInstanceSerializer

User = get_user_model()


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = FullUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.get_queryset().get()


class ErrorInstanceViewSet(viewsets.ViewSet):
    """
    ViewSet for creating or retrieving ErrorInstances.
    """

    serializer_class = ErrorInstanceSerializer
    queryset = ErrorInstance.objects.all()

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass
