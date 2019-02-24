from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User

from business_judge.problem.models import (
    Problem
)
from business_judge.submission.models import Submission

from business_judge.submission.services import (
    create_submission
)

class CreateSubmissionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.problem = Problem.objects.create(
            name="problem1",
            max_score=100
        )
        self.service = create_submission

    @patch('business_judge.submission.services.get_problem_by_id')
    @patch('business_judge.submission.services.get_user_by_username')
    def test_create_submission(
            self,
            get_user_by_username_mock,
            get_problem_by_id_mock
    ):
        get_user_by_username_mock.return_value = self.user
        get_problem_by_id_mock.return_value = self.problem
        
        self.assertEqual(
            0,
            Submission.objects.count()
        )

        submission = self.service(
            user=self.user.username,
            problem=self.problem.id,
            source_code=None
        )

        self.assertEqual(
            1,
            Submission.objects.count()
        )
        self.assertEqual(
            submission,
            Submission.objects.first()
        )