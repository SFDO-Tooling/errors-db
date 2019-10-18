from .serializers import FullUserSerializer
from errors_db.api.models import ErrorInstance, Solution
from errors_db.api.serializers import ErrorInstanceSerializer

from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

User = get_user_model()


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = FullUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.get_queryset().get()


class ErrorInstanceViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """
    ViewSet for creating ErrorInstances.
    """

    permission_classes = [AllowAny]
    queryset = ErrorInstance.objects.all()
    serializer_class = ErrorInstanceSerializer

    def create(self, request):
        error_msg = request.data["message"]
        context = request.data["context"]
        stacktrace = request.data["stacktrace"]

        ErrorInstance.objects.create(
            message=error_msg, context=context, stacktrace=stacktrace
        )

        solutions = Solution.objects.filter(situation__error_msg=error_msg)
        data = {"solutions": "No solution found."}
        if solutions.count():
            data["solutions"] = [value for value in solutions.values()]
        return Response(data, status=status.HTTP_201_CREATED)
