from datetime import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .selectors import *

def get_or_create_token(
        *,
        user: User
) -> Token:

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
