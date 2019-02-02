from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction

from .selectors import *
from .models import Profile, Course


def create_profile(
        *,
        username: str,
        course_id: int
) -> Profile:

    user = get_user_by_username(username=username)

    course = get_course_by_id(id=course_id)

    profile = Profile(
        user=user,
        course=course
    )
    profile.full_clean()
    profile.save()

    return profile


@transaction.atomic
def create_user(
        *,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
        course: int
) -> User:

    if User.objects.filter(email=email).exists() \
            or User.objects.filter(username=username).exists():
        raise ValidationError('User already exists.')

    course = get_course_by_id(id=course)

    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
    )
    user.set_password(password)
    user.full_clean()
    user.save()

    create_profile(
        username=user.username,
        course_id=course.id
    )
    # TODO - send_confirmation_email(user=user)

    return user
