from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from business_judge.user.selectors import get_user_by_username


class GetUserByUsernameTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.selector = get_user_by_username

    def test_get_user_by_username(self):

        self.assertEqual(
            self.user,
            self.selector(username=self.user.username)
        )

    def test_get_user_not_exists(self):

        with self.assertRaises(ValidationError):
            self.selector(username=None)
