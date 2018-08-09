from rest_framework import serializers
from App.models import Profile
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