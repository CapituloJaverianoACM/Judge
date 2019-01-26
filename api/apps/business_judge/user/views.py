from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services import *


class UserViewSet(viewsets.ViewSet):

    class InputSerializer(serializers.Serializer):
        firstname = serializers.CharField()
        lastname = serializers.CharField()
        username = serializers.CharField()
        email = serializers.CharField()
        password = serializers.CharField()
        course = serializers.IntegerField()

    def post(self, request, *args, **kwargs):
        user_serializer = self.InputSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        create_user(**user_serializer)

        return Response(status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action == 'post':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]