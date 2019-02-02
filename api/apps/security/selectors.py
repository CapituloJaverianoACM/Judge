from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


def get_token_by_user(
        *,
        user: User
) -> Token:

    token = Token.objects.filter(user=user)
    if not token.exists():
        raise ValidationError('Token not exist')

    return token[0]