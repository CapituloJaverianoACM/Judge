from rest_framework import serializers
from .model import Problem


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'

    def create(self, validated_data):
        return Problem.objects.create(**validated_data)