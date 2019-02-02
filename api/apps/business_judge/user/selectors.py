from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Course


def get_course_by_id(
        *,
        id: int
) -> Course:

    course = Course.objects.filter(id=id)
    if not course.exists():
        raise ValidationError('Course not exist')

    return course[0]


def get_user_by_username(
        *,
        username: str
) -> User:

    user = User.objects.filter(username=username)
    if not user.exists():
        raise ValidationError('User not exist')

    return user[0]
