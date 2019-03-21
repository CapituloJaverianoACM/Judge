from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError

from .models import Submission


def get_all_submissions() -> QuerySet:
    return Submission.objects.all().order_by('-created')


def get_submission_by_id(
        *,
        id: int
) -> QuerySet:
    submission = Submission.objects.filter(
        id=id
    )
    if not submission.exists():
        raise ValidationError("Submission not exists")
    return submission[0]