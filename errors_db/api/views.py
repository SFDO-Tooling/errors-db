import logging
from .serializers import FullUserSerializer
from errors_db.api.models import ErrorInstance, Solution
from errors_db.api.serializers import ErrorInstanceSerializer
from errors_db.api.search import ErrorSearch

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


class ErrorInstanceViewSet(viewsets.GenericViewSet):
    """
    ViewSet for creating ErrorInstances.
    """

    logger = logging.getLogger(__name__)
    permission_classes = [AllowAny]
    queryset = ErrorInstance.objects.all()
    serializer_class = ErrorInstanceSerializer

    def create(self, request):
        self.logger.info(f"Request received: {request.id}")
        context = request.data["context"]
        error_msg = request.data["message"]
        stacktrace = request.data["stacktrace"]

        ErrorInstance.objects.create(
            message=error_msg, context=context, stacktrace=stacktrace
        )

        solutions = ErrorSearch.get_solutions(error_msg, stacktrace, context)

        response = self._get_response(solutions)
        self.logger.info(f"Sending Response {response} for request_id {request.id}")
        return response

    def _get_response(self, solutions):
        response_data = {}
        if not solutions:
            response_data["solutions"] = "No solutions found."
        else:
            response_data["solutions"] = [value for value in solutions.values()]
        return Response(response_data, status=status.HTTP_201_CREATED)
