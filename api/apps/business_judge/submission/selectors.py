from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError
from django.http import HttpResponse

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


def get_source_code_by_id(
        *,
        id: int
):
    submission = get_submission_by_id(
        id=id
    )
    filename = submission.source_code.path
    if not filename:
        raise ValidationError("Source code not exists")
    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(),
                                content_type='application/x-www-form'
                                             '-urlencoded')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/x-www-form-urlencoded; ' \
                                   'charset=utf-8 '
        return response
