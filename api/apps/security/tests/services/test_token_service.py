from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError

from security.services import (
    get_or_create_token,
    delete_token_by_user
)


class GetOrCreateTokenTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Test User',
            email='TestUser@test.com'
        )
        self.service = get_or_create_token

    def test_create_token(self):

        self.assertEqual(0, Token.objects.count())

        token = self.service(
            user=self.user
        )

        self.assertEqual(1, Token.objects.count())
        self.assertEqual(
            token,
            Token.objects.first()
        )

    def test_get_token(self):

        self.assertEqual(0, Token.objects.count())

        token_init = Token.objects.create(
            user=self.user
        )

        token = self.service(
            user=self.user
        )

        self.assertEqual(1, Token.objects.count())
        self.assertEqual(
            token,
            token_init
        )

    def test_create_token_not_user(self):

        self.assertEqual(0, Token.objects.count())

        with self.assertRaises(ValidationError):
            self.service(user=None)


class DeleteTokenTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Test User',
            email='TestUser@test.com'
        )
        # TODO - create token with date warning
        self.token = Token.objects.create(
            user=self.user
        )
        self.service = delete_token_by_user

    @patch('security.services.get_token_by_user')
    def test_delete_token(
            self,
            get_token_by_user
    ):
        get_token_by_user.return_value = self.token

        self.assertEqual(1, Token.objects.count())

        self.service(user=self.user)

        self.assertEqual(0, Token.objects.count())
