from rest_framework import status, viewsets
from App.description.serializer import DescriptionSerializer
from rest_framework.response import Response
from App.user.permissions import AdminPermissions


class DescriptionViewSet(viewsets.ViewSet):
    permission_classes = [AdminPermissions]
    '''
    def create(self, request):
        description_serializer = DescriptionSerializer(data=request.data)
        if description_serializer.is_valid():
            description_serializer.create(request.data)
            return Response(
                description_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            description_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    '''
