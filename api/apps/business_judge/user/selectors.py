from .models import Course
from django.core.exceptions import ValidationError


def get_course_by_id(
        *,
        id: int
) -> Course:

    course = Course.objects.filter(id=id)
    if not course.exists():
        raise ValidationError('Course not exist')

    return course[0]
