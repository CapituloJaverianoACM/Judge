from rest_framework import  status, viewsets
from App.problem.serializer import ProblemSerializer
from rest_framework.response import Response
from App.user.permissions import AdminPermissions

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