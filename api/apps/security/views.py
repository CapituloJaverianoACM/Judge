from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny

from .services import *
from utils.mixins import ExceptionHandlerMixin


class ObtainExpiringAuthToken(
    ExceptionHandlerMixin,
    ObtainAuthToken
):

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        response_data = {
            'token': get_or_create_token(user=user).key
        }
        return Response(
            response_data,
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        delete_token_by_user(user=request.user)
        return Response(
            "OK",
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]