from django.contrib.auth.models import User
from .models import Profile


def create_profile(
        *,
        user: User,
        course: int
) -> Profile:

    profile = Profile(
        user=user,
        course=course
    )
    profile.full_clean()
    profile.save()

    return profile


def create_user(
        *,
        firstname: str,
        lastname: str,
        username: str,
        email: str,
        password: str,
        course: int
) -> User:
    user = User(
        firstname=firstname,
        lastname=lastname,
        username=username,
        email=email,
    )
    user.full_clean()
    user.set_password(password)
    user.save()

    create_profile(user=user, course=course)
    # TODO - send_confirmation_email(user=user)

    return user