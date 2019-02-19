from django.db.models.query import QuerySet

from business_judge.test_case.models import (
    TestCaseModel,
    Problem
)


def get_sample_test(
        *,
        problem: Problem
) -> QuerySet:

    return TestCaseModel.objects.filter(
        problem=problem,
        is_sample=True
    )
