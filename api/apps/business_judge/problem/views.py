from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .selectors import (
    get_all_problems
)
from .models import (
    Tag,
    Problem
)
from utils.mixins import ExceptionHandlerMixin
from utils.serializers import inline_serializer


class ProblemGeneralViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):

    class OutputSerializer(serializers.ModelSerializer):
        score = serializers.FloatField()
        tags = inline_serializer(
            many=True,
            fields={
                'name': serializers.CharField(),
            }
        )

        class Meta:
            model = Problem
            fields = ('name', 'score', 'tags')

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
