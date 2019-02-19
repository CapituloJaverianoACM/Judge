from rest_framework import (
    status,
    serializers,
    viewsets
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from django.contrib.auth.models import User

from .services import (
    get_or_create_token,
    delete_token_by_user
)
from utils.mixins import ExceptionHandlerMixin


class ObtainExpiringAuthToken(
    ExceptionHandlerMixin,
    ObtainAuthToken,
    viewsets.ViewSet
):

    class OutputUserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = (
                'first_name',
                'last_name',
                'username',
                'email'
            )

    def post(self, request, **kwargs):
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

    def get(self, request):

        user_serializer = self.OutputUserSerializer(
            request.user
        )
        return Response(
            user_serializer.data,
            status=status.HTTP_202_ACCEPTED
        )

    def get_permissions(self):
        if self.action == 'post':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
