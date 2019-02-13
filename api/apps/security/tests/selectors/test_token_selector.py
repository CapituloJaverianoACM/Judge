from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from security.selectors import (
    get_token_by_user
)


class GetTokenByUserTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Test User',
            email='TestUser@test.com'
        )
        self.token = Token.objects.create(
            user=self.user
        )
        self.selector = get_token_by_user

    def test_get_token_by_user(self):

        self.assertEqual(
            self.token,
            self.selector(user=self.user)
        )

    def test_get_token_user_not_exists(self):

        with self.assertRaises(ValidationError):
            self.selector(user=None)

    def test_get_not_exists_token_(self):

        user_temp = User.objects.create_user(
            username='Temp user',
            email='Tempuser@test.com'
        )

        with self.assertRaises(ValidationError):
            self.selector(user=user_temp)
