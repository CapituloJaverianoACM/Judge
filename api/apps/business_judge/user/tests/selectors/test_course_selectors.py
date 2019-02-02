from django.test import TestCase
from django.core.exceptions import ValidationError

from business_judge.user.selectors import get_course_by_id
from business_judge.user.models import Course


class GetCourseByIdTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name="Test Course")
        self.selector = get_course_by_id

    def test_get_course_by_id(self):

        self.assertEqual(
            self.course,
            self.selector(id=self.course.id)
        )

    def test_get_course_not_exists(self):

        with self.assertRaises(ValidationError):
            self.selector(id=None)
