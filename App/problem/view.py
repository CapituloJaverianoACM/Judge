from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from App.problem.model import Problem
from App.problem.serializer import ProblemSerializer
from rest_framework.response import Response
from App.user.permissions import AdminPermissions
from django.shortcuts import get_object_or_404


class ProblemViewSet(viewsets.ViewSet):

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

    def delete(self, request):
        problem_id = request.data.get('id', -1)
        get_object_or_404(Problem, id=problem_id).delete()
        return Response(
            "Ok delete",
            status=status.HTTP_200_OK
        )

    def get(self, request):
        problems_serializer = ProblemSerializer(
            Problem.objects.all(),
            many=True
        )
        return Response(
            problems_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_by_id(self, request, id):
        problem = get_object_or_404(Problem, id=id)
        problem_serializer = ProblemSerializer(
            problem
        )
        return Response(
            problem_serializer.data,
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        if self.action == 'get':
            permission_classes = [IsAuthenticated]
        elif self.action == 'get_by_id':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AdminPermissions]
        return [permission() for permission in permission_classes]
