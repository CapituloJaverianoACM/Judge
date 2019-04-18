from rest_framework import status, viewsets, serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from utils.mixins import ExceptionHandlerMixin

from .selectors import (
    get_input_file_by_id,
    get_output_file_by_id
)


class TestCaseViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):

    def get_input_by_id(self, request, id):

        test_input = get_input_file_by_id(
            id=id
        )
        return test_input

    def get_output_by_id(self, request, id):

        test_output = get_output_file_by_id(
            id=id
        )
        return test_output

    def get_permissions(self):
        if self.action == 'get_input_by_id':
            permission_classes = [IsAdminUser]
        elif self.action == 'get_output_by_id':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
