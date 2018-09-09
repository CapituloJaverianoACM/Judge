from rest_framework import serializers

from App.description.serializer import DescriptionSerializer
from .model import Problem


class ProblemSerializer(serializers.ModelSerializer):

    description = DescriptionSerializer(required=False)

    class Meta:
        model = Problem
        fields = '__all__'

    def create(self, validated_data):
        description_serializer = DescriptionSerializer(data={})
        if description_serializer.is_valid():
            description = description_serializer.create({})
        validated_data['description'] = description
        problem = Problem.objects.create(**validated_data)
        return problem
