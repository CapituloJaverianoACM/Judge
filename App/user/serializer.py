from rest_framework import serializers
from .model import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.Field(write_only=True, required=False)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data, user):
        return Profile.objects.create(user=user, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        profile = ProfileSerializer(data=profile_data)
        if profile.is_valid():
            profile.create(profile_data, user)
        return user

    def update(self, instance, validated_data):

        if validated_data.get('profile', False):
            profile_serializer = ProfileSerializer(data=validated_data['profile'])
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.update(instance.profile, validated_data['profile'])
            validated_data.pop('profile')

        if validated_data.get('password', False):
            instance.set_password(validated_data['password'])

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance

