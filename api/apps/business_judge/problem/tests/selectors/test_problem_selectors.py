from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import tempfile

from business_judge.problem.models import (
    Problem,
    Tag
)
from business_judge.submission.models import (
    Submission
)
from business_judge.test_case.models import (
    TestCaseModel
)

from business_judge.problem.selectors import (
    get_all_problems,
    get_problem_by_id
)


class GetAllProblemsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.problem = Problem.objects.create(
            name="problem1",
            max_score=100
        )
        self.tag = Tag.objects.create(
            name='Hard'
        )
        self.problem.tags.add(self.tag)
        self.source_code = tempfile.NamedTemporaryFile()
        self.addTestCase(0)
        self.addTestCase(1)
        self.addTestCase(2)
        self.addTestCase(3)
        self.selector = get_all_problems

    def test_get_problems_without_submissions(self):

        response = self.selector(
            username=self.user.username
        )
        self.assertEqual(
            response.count(),
            1
        )
        self.assertEqual(
            response[0].name,
            self.problem.name
        )
        self.assertEqual(
            response[0].score,
            0
        )
        self.assertEqual(
            response[0].tags.count(),
            1
        )
        self.assertEqual(
            response[0].tags.all()[0].id,
            self.tag.id
        )

    def test_get_problems_with_only_one_submission(self):

        Submission.objects.create(
            verdict='AC',
            user=self.user,
            problem=self.problem,
            cases_passed=3,
            source_code=self.source_code.name
        )

        response = self.selector(
            username=self.user.username
        )
        self.assertEqual(
            response.count(),
            1
        )
        self.assertEqual(
            response[0].name,
            self.problem.name
        )
        self.assertEqual(
            response[0].score,
            3 / 4
        )
        self.assertEqual(
            response[0].tags.count(),
            1
        )
        self.assertEqual(
            response[0].tags.all()[0].id,
            self.tag.id
        )

    def test_get_problems_with_more_than_one_submission(self):

        Submission.objects.create(
            verdict='AC',
            user=self.user,
            problem=self.problem,
            cases_passed=3,
            source_code=self.source_code.name
        )

        Submission.objects.create(
            verdict='AC',
            user=self.user,
            problem=self.problem,
            cases_passed=4,
            source_code=self.source_code.name
        )

        response = self.selector(
            username=self.user.username
        )
        response = self.selector(
            username=self.user.username
        )
        self.assertEqual(
            response.count(),
            1
        )
        self.assertEqual(
            response[0].name,
            self.problem.name
        )
        self.assertEqual(
            response[0].score,
            1.0
        )
        self.assertEqual(
            response[0].tags.count(),
            1
        )
        self.assertEqual(
            response[0].tags.all()[0].id,
            self.tag.id
        )

    def addTestCase(self, number):
        TestCaseModel.objects.create(
            number=number,
            file_input=self.source_code.name,
            file_output=self.source_code.name,
            problem=self.problem,
            explanation="."
        )


class GetProblemByIdTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.problem = Problem.objects.create(
            name="problem1",
            max_score=100
        )
        self.tag = Tag.objects.create(
            name='Hard'
        )
        self.problem.tags.add(self.tag)
        self.source_code = tempfile.NamedTemporaryFile()
        self.addTestCase(0, True)
        self.addTestCase(1, True)
        self.addTestCase(2)
        self.addTestCase(3)
        self.selector = get_problem_by_id

    def test_get_problem_by_id(self):

        response = self.selector(
            id=self.problem.id
        )

        self.assertEqual(
            response.id,
            self.problem.id
        )

    def test_get_problem_not_exists(self):

        with self.assertRaises(ValidationError):
            self.selector(id=None)

    def addTestCase(
            self,
            number,
            is_sample=False
    ):
        TestCaseModel.objects.create(
            number=number,
            file_input=self.source_code.name,
            file_output=self.source_code.name,
            problem=self.problem,
            explanation=".",
            is_sample=is_sample
        )
