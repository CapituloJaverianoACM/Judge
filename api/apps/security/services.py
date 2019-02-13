from datetime import datetime

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .selectors import (
    get_token_by_user
)


def get_or_create_token(
        *,
        user: User
) -> Token:

    if not user:
        raise ValidationError('User not exists.')

    token, created = Token.objects.get_or_create(
        user=user
    )

    token.created = datetime.utcnow()
    token.full_clean()
    token.save()

    return token


def delete_token_by_user(
        *,
        user: User
) -> None:

    token = get_token_by_user(user=user)
    token.delete()
