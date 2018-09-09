from rest_framework import status, viewsets

from App.problem.model import Problem
from App.problem.serializer import ProblemSerializer
from rest_framework.response import Response
from App.user.permissions import AdminPermissions
from django.shortcuts import get_object_or_404


class ProblemViewSet(viewsets.ViewSet):
    permission_classes = [AdminPermissions]

    def create(self, request):
        problem_serializer = ProblemSerializer(data=request.data)
        if problem_serializer.is_valid():
            problem_serializer.create(request.data)
            return Response(
                problem_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            problem_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        problem_id = request.data.get('id', -1)
        problem = get_object_or_404(Problem, id=problem_id)
        problem_serializer = ProblemSerializer(data=request.data, partial=True)
        problem_serializer.is_valid(raise_exception=True)
        problem_serializer.update(problem, request.data)
        return Response(
            "Update problem",
            status=status.HTTP_200_OK
        )
