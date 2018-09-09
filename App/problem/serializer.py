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

    def update(self, instance, validated_data):

        if validated_data.get('description', False):
            description_serializer = DescriptionSerializer(
                data=validated_data['description']
            )
            description_serializer.is_valid(raise_exception=True)
            description_serializer.update(
                instance.description,
                validated_data['description']
            )
            validated_data.pop('description')

        instance.max_score = validated_data.get(
            'max_score',
            instance.max_score
        )
        instance.difficulty = validated_data.get(
            'difficulty',
            instance.difficulty
        )
        instance.time_limit = validated_data.get(
            'time_limit',
            instance.time_limit
        )
        instance.theme = validated_data.get(
            'theme',
            instance.theme
        )
        instance.template = validated_data.get(
            'template',
            instance.template
        )
        instance.link_source = validated_data.get(
            'link_source',
            instance.link_source
        )
        instance.is_original = validated_data.get(
            'is_original',
            instance.is_original
        )
        instance.save()
        return instance
