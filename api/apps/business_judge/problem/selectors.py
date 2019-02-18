from django.db.models.query import QuerySet
from django.db.models import Max, Count, Value, Case, FloatField
from django.db.models.functions import Greatest, Coalesce

from .models import Problem


def get_all_problems(
        *,
        username: str
) -> QuerySet:
    problems_tried = Problem.objects. \
        filter(
         submission__user__username=username
        )\
        .annotate(
            score=
            Case(
                default=
                Coalesce(
                    Max('submission__cases_passed'),
                    0
                ) / Greatest(
                    Count(
                        'test_case',
                        distinct=True
                    ),
                    1.0
                ),
                output_field=FloatField()

            )
        )

    problems_not_tried = Problem.objects. \
        exclude(
            submission__user__username=username
        ) \
        .annotate(
            score=Case(
                default=Value(0.0),
                output_field=FloatField()
            )
        )

    problems = problems_tried.union(problems_not_tried)
    return problems
