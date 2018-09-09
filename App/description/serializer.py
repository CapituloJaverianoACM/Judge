from rest_framework import serializers
from App.problem.model import Problem
from .model import Description, TestCase
from django.shortcuts import get_object_or_404


class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = '__all__'

    def create(self, validated_data):
        return Description.objects.create(**validated_data)


class TestCaseSerializer(serializers.ModelSerializer):

    fileIn = serializers.FileField(write_only=True)
    fileOut = serializers.FileField(write_only=True)
    description = DescriptionSerializer(required=False)
    problem = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = TestCase
        fields = '__all__'

    def create(self, validated_data):
        problem_id = validated_data['problem']
        problem = get_object_or_404(Problem, id=problem_id)
        validated_data.pop('problem')
        description = get_object_or_404(Description, id=problem.description.id)
        return TestCase.objects.create(**validated_data,
                                       description=description)
