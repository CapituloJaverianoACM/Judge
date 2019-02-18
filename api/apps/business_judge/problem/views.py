from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .selectors import (
    get_all_problems
)

from utils.mixins import ExceptionHandlerMixin


class ProblemGeneralViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):
    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        score = serializers.FloatField()
        tags = serializers.ListField()

    def get(self, request):

        problems = get_all_problems(
            username=request.user.username
        )
        problems_serializer = self.OutputSerializer(
            problems,
            many=True
        )
        return Response(
            problems_serializer.data,
            status=status.HTTP_200_OK
        )
