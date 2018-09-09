from rest_framework import status, viewsets

from App.submission.model import Submission
from App.submission.serializer import SubmissionSerializer
from rest_framework.response import Response


class SubmissionViewSet(viewsets.ViewSet):

    def create(self, request):
        request.data['user'] = request.user.id
        submission_serializer = SubmissionSerializer(data=request.data)
        submission_serializer.is_valid(raise_exception=True)
        submission_serializer.save()
        return Response(
            submission_serializer.data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        submissions_serializer = SubmissionSerializer(
            Submission.objects.all(),
            many=True
        )
        return Response(
            submissions_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_by_user(self, request, id):
        submissions_serializer = SubmissionSerializer(
            Submission.objects.filter(user=id),
            many=True
        )
        return Response(
            submissions_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_by_problem(self, request, id):
        submissions_serializer = SubmissionSerializer(
            Submission.objects.filter(problem=id),
            many=True
        )
        return Response(
            submissions_serializer.data,
            status=status.HTTP_200_OK
        )
