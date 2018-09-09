from rest_framework import serializers
from App.problem.model import Problem
from .model import Description
from django.shortcuts import get_object_or_404


class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = '__all__'

    def create(self, validated_data):
        return Description.objects.create(**validated_data)
