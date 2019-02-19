from django.db.models.query import QuerySet
from django.db.models import Max, Count, Value, Case, FloatField
from django.db.models.functions import Greatest, Coalesce
from django.core.exceptions import ValidationError

from .models import Problem


def get_problems_tried(
        *,
        username: str
) -> QuerySet:
    return Problem.objects.\
        filter(
            submission__user__username=username
        )\
        .annotate(
            score=Case
            (
                default=Coalesce
                (
                    Max('submission__cases_passed'),
                    0
                ) / Greatest(
                    Count(
                        'test_cases',
                        distinct=True
                    ),
                    1.0
                ),
                output_field=FloatField()

            )
        )


def get_problems_not_tried(
        *,
        username: str
) -> QuerySet:
    return Problem.objects.\
        exclude(
            submission__user__username=username
        )\
        .annotate(
            score=Case
            (
                default=Value(0.0),
                output_field=FloatField()
            )
        )


def get_all_problems(
        *,
        username: str
) -> QuerySet:
    problems_tried = get_problems_tried(
        username=username
    )

    problems_not_tried = get_problems_not_tried(
        username=username
    )

    problems = problems_tried.union(problems_not_tried)
    return problems


def get_problem_by_id(
        *,
        id: int
) -> QuerySet:
    problem = Problem.objects.filter(
        id=id,
    )
    if not problem.exists():
        raise ValidationError("Problem not exists")
    return problem[0]
