from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from business_judge.problem.models import (
    Problem
)
from business_judge.submission.models import Submission

from business_judge.submission.selectors import (
    get_all_submissions
)


class GetAllSubmissionsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.problem = Problem.objects.create(
            name="problem1",
            max_score=100
        )
        self.submission = Submission.objects.create(
            user=self.user,
            problem=self.problem,
        )
        self.selector = get_all_submissions

    def test_get_all_submissions(self):

        submissions = self.selector()

        self.assertEqual(
            submissions.count(),
            1
        )
        self.assertEqual(
            submissions[0],
            self.submission
        )

    def test_order_submission(self):
        submission_add = Submission.objects.create(
            self.submission
        )
        submissions = self.selector()
        self.assertEqual(
            submissions.count(),
            2
        )
        self.assertEqual(
            submissions[0],
            submission_add
        )