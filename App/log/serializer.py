from .model import Log
from rest_framework import serializers


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = '__all__'

    def create(self, validated_data):
        return Log.objects.create(**validated_data)
