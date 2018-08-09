from rest_framework import status, viewsets
from App.serializers.log_serializer import LogSerializer
from App.services import log_service
from rest_framework.response import Response

class LogViewSet(viewsets.ViewSet):

    def list(self, request):
        log_serializer = LogSerializer(
            log_service.getAll(),
            many = True
        )
        return Response(
            log_serializer.data,
            status=status.HTTP_200_OK
        )


    def create(self, request):
        log_serializer = LogSerializer(data=self.request.data)
        if log_serializer.is_valid():
            log_serializer.create(log_serializer.data)
            return Response(
             log_serializer.data,
             status=status.HTTP_201_CREATED
            )
        return Response(
            log_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )