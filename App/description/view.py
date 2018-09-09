from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from App.description.serializer import DescriptionSerializer, TestCaseSerializer
from rest_framework.response import Response
from App.user.permissions import AdminPermissions
from .model import TestCase
import os

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


class TestCasesViewSet(viewsets.ViewSet):
    permission_classes = [AdminPermissions]

    def create(self, request):
        test_case_serializer = TestCaseSerializer(data=request.data)
        test_case_serializer.is_valid(raise_exception=True)
        test_case_serializer.save()
        return Response(
            test_case_serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        test_case_id = request.data.get('id', -1)
        test_case_serializer = TestCaseSerializer(data=request.data, partial=True)
        test_case_serializer.is_valid(raise_exception=True)
        test_case = get_object_or_404(TestCase, id=test_case_id)
        if request.data.get('fileIn', False):
            os.remove(test_case.fileIn.path)
        if request.data.get('fileOut', False):
            os.remove(test_case.fileOut.path)
        test_case_serializer.update(test_case, request.data)
        return Response(
            test_case_serializer.data,
            status=status.HTTP_200_OK
        )
