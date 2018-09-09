from rest_framework import status, viewsets
from .serializer import CommmentSerializer
from rest_framework.response import Response


class CommmentViewSet(viewsets.ViewSet):

    def create(self, request):
        request.data['user'] = request.user.id
        comment_serializer = CommmentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.create(request.data)
            return Response(
                comment_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            comment_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
