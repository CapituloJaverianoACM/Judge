from rest_framework import serializers
from .model import Submission, QueueSubmission
from App.user.model import User
from App.problem.model import Problem
from django.shortcuts import get_object_or_404


class SubmissionSerializer(serializers.ModelSerializer):

    source_code = serializers.FileField()

    class Meta:
        model = Submission
        fields = '__all__'

    def create(self, validated_data):
        user_id = validated_data['user']
        problem_id = validated_data['problem']
        # validated_data['user'] =
        #get_object_or_404(User, id=user_id)
        # validated_data['problem'] =
        #get_object_or_404(Problem, id=problem_id)
        submission = Submission.objects.create(**validated_data)
        QueueSubmission.objects.create(submission=submission)
        return submission
