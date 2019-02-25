from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User

from .services import (
    create_user
)
from .selectors import (
    get_scoreboard_general
)
from utils.mixins import ExceptionHandlerMixin


class UserViewSet(ExceptionHandlerMixin, viewsets.ViewSet):

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        username = serializers.CharField()
        email = serializers.CharField()
        password = serializers.CharField()
        course = serializers.IntegerField()
        phone = serializers.CharField()

    def post(self, request, *args, **kwargs):
        user_serializer = self.InputSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        create_user(**user_serializer.validated_data)

        return Response(
            "Ok",
            status=status.HTTP_201_CREATED
        )

    def get_permissions(self):
        if self.action == 'post':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ScoreBoardViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):
    permission_classes = [AllowAny]

    class OuputSerializer(serializers.ModelSerializer):
        score = serializers.FloatField()

        class Meta:
            model = User
            fields = (
                'first_name',
                'last_name',
                'username',
                'score'
            )

    def get_all(self, request):
        scoreboard = self.OuputSerializer(
            get_scoreboard_general(),
            many=True
        )

        return Response(
            scoreboard.data,
            status=status.HTTP_200_OK
        )
