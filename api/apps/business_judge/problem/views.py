from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .selectors import (
    get_all_problems,
    get_problem_by_id
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
            fields = ('id', 'name', 'score', 'tags')

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


class ProblemSingleViewSet(
    ExceptionHandlerMixin,
    viewsets.ViewSet
):

    class OutputSerializer(serializers.ModelSerializer):
        tags = inline_serializer(
            many=True,
            fields={
                'name': serializers.CharField(),
            }
        )
        description = inline_serializer(
            fields={
                'statement': serializers.CharField(),
                'input_format': serializers.CharField(),
                'output_format': serializers.CharField(),
            }
        )
        test_cases = inline_serializer(
            many=True,
            source="get_sample_test",
            fields={
                'number': serializers.IntegerField(),
                'explanation': serializers.CharField(),
                # TODO - return input and output
                'input': serializers.CharField(),
                'output': serializers.CharField(),
            }
        )

        class Meta:
            model = Problem
            fields = (
                'id',
                'name',
                'max_score',
                'tags',
                'description',
                'test_cases'
            )

    def get(self, request, id):

        problem = get_problem_by_id(
            id=id
        )
        problem_serializer = self.OutputSerializer(
            problem
        )
        return Response(
            problem_serializer.data,
            status=status.HTTP_200_OK
        )
