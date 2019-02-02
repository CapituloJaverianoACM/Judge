from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from business_judge.user.services import create_user
from business_judge.user.models import Profile, Course


class CreateUserTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Test User',
            email='TestUser@test.com'
        )
        self.course = Course.objects.create(name="Test Course")
        self.service = create_user
        self.data = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test',
            'course': self.course.id
        }

    @patch('business_judge.user.services.create_profile')
    @patch('business_judge.user.services.get_course_by_id')
    def test_create_user(
            self,
            get_course_by_id_mock,
            create_profile_mock,
    ):

        get_course_by_id_mock.return_value = self.course
        create_profile_mock.return_value = True

        self.assertEqual(1, User.objects.count())

        user = self.service(
            **self.data
        )

        self.assertEqual(2, User.objects.count())
        self.assertEqual(
            user,
            User.objects.get(username=user.username)
        )

    def test_create_user_exists_username(self):

        self.data['username'] = self.user.username

        with self.assertRaises(ValidationError):
            self.service(**self.data)

    def test_create_user_exists_email(self):

        self.data['email'] = self.user.email

        with self.assertRaises(ValidationError):
            self.service(**self.data)
