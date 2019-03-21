from rest_framework import status, viewsets, serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import (
    Submission
)
from .selectors import (
    get_all_submissions,
    get_source_code_by_id
)
from .services import (
    create_submission
)

from utils.mixins import ExceptionHandlerMixin


class SubmissionViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):
    class OutputSerializer(serializers.ModelSerializer):
        user = serializers.CharField(
            source='get_username'
        )
        total_cases = serializers.IntegerField(
            source='get_total_cases'
        )

        class Meta:
            model = Submission
            fields = (
                'verdict',
                'user',
                'problem',
                'cases_passed',
                'total_cases',
                'created'
            )

    class InputSerializer(serializers.Serializer):
        problem = serializers.IntegerField()
        user = serializers.CharField()
        source_code = serializers.FileField()
        language = serializers.CharField()

    def list(self, request):
        submissions_serializer = self.OutputSerializer(
            get_all_submissions(),
            many=True
        )
        return Response(
            submissions_serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):

        request.data['user'] = request.user.username
        submission_serializer = self.InputSerializer(
            data=request.data
        )
        submission_serializer.is_valid(
            raise_exception=True
        )
        create_submission(
            **submission_serializer.validated_data
        )

        return Response(
            'Ok',
            status=status.HTTP_201_CREATED
        )

    def get_source_code(self, request, id):

        file = get_source_code_by_id(
            id=id
        )
        return file

    def get_permissions(self):
        if self.action == 'get_source_code':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
