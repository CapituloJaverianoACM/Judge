from django.db.models.query import QuerySet

from .models import Submission


def get_all_submissions() -> QuerySet:
    return Submission.objects.all().order_by('-created')