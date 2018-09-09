from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from App.user.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from App.user.permissions import AdminPermissions


class UserViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.create(request.data)
            return Response(
                user_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        user = request.user
        user_serializer = UserSerializer(data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.update(user, request.data)
        return Response(
            "Update",
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        User.objects.get(id=request.user.id).delete()
        return Response(
            "Ok delete",
            status=status.HTTP_200_OK
        )

    def delete_by_id(self, request):
        user_id = request.data.get('id', -1)
        get_object_or_404(User, id=user_id).delete()
        return Response(
            "Ok delete",
            status=status.HTTP_200_OK
        )

    def get(self, request):
        users_serializer = UserSerializer(
            User.objects.all(),
            many=True
        )
        return Response(
            users_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_by_id(self, request, id):
        user = get_object_or_404(User, id=id)
        user_serializer = UserSerializer(
            user
        )
        return Response(
            user_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'delete_by_id':
            permission_classes = [AdminPermissions]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
