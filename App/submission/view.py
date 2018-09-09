from rest_framework import status, viewsets

from App.submission.model import Submission
from App.submission.serializer import SubmissionSerializer
from rest_framework.response import Response


class SubmissionViewSet(viewsets.ViewSet):

    def create(self, request):
        request.data['user'] = request.user.id
        submission_serializer = SubmissionSerializer(data=request.data)
        if submission_serializer.is_valid():
            submission_serializer.create(request.data)
            return Response(
                submission_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            submission_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
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
