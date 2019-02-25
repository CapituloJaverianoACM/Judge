from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User


from business_judge.user.services import create_profile
from business_judge.user.models import Profile, Course


class CreateProfileTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Test User')
        self.course = Course.objects.create(name="Test Course")
        self.service = create_profile

    @patch('business_judge.user.services.get_course_by_id')
    @patch('business_judge.user.services.get_user_by_username')
    def test_create_profile(
            self,
            get_user_by_username_mock,
            get_course_by_id_mock,
    ):

        get_user_by_username_mock.return_value = self.user
        get_course_by_id_mock.return_value = self.course

        self.assertEqual(0, Profile.objects.count())

        profile = self.service(
            username=self.user.username,
            course_id=self.course.id,
            phone="12345"
        )

        self.assertEqual(1, Profile.objects.count())
        self.assertEqual(profile, Profile.objects.first())
