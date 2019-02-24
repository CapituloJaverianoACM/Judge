from rest_framework import status, viewsets, serializers
from rest_framework.response import Response

from .models import (
    Submission
)
from .selectors import (
    get_all_submissions
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

        class Meta:
            model = Submission
            fields = (
                'verdict',
                'user',
                'problem',
                'cases_passed',
                'created'
            )

    class InputSerializer(serializers.Serializer):
        problem = serializers.IntegerField()
        user = serializers.CharField()
        source_code = serializers.FileField()

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
