from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from .serializers import FullUserSerializer
from errors_db.api.models import Error
from errors_db.api.serializers import ErrorSerializer

User = get_user_model()


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = FullUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.get_queryset().get()


def error_list(request):
    """
    List all error instances, or create a new error instance.
    """
    if request.method == "GET":
        errors = Error.objects.all()
        serializer = ErrorSerializer(errors, many=True)

        # This Works
        return JsonResponse(serializer.data, safe=False)

        # This Works
        return JsonResponse(serializer.data[0])

        # This doesn't work
        return JsonResponse(serializer.data)

    # elif request.method == "POST":
    # data = JsonParser().parse(request)
    # serializer = ErrorSerializer(data=data)
    # if serializer.is_valid():
    # serializer.save()
    # return JsonResponse(serializer.data, status=201)
    # return JsonResponse(serializer.errors, status=400)


def error_detail(request, pk):
    """
    Retrieve an error instance
    """
    try:
        error = Error.objects.get(pk=pk)
    except Error.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ErrorSerializer(error)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JsonParser().parse(request)
        serializer = ErrorSerializer(error, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors, status=400)
