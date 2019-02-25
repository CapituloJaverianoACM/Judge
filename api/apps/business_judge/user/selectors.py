from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from django.db.models import (
    Max,
    Count,
    Case,
    FloatField,
    F,
    Sum,
    Subquery,
    OuterRef,
    Q
)
from django.db.models.functions import (
    Greatest,
    Coalesce
)
from business_judge.problem.selectors import (
    get_all_problems
)

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


def get_scoreboard_general(
) -> QuerySet:

    '''
    scoreboard = User.objects.all().annotate(
        problem=F('submission__problem')
    ).annotate(
        score_temp=Case
            (
            default=Coalesce
                        (
                        Max('submission__cases_passed'),
                        0
                    ) / Greatest(
                Count(
                    'submission__problem__test_cases',
                    distinct=True
                ),
                1.0
            ) * F('submission__problem__max_score'),
            output_field=FloatField()

        ),
    )
    '''
    scoreboard = User.objects.raw(
        '''
            SELECT "querytable"."id", "querytable"."username",
            SUM("score_temp") as "score"
            FROM (
            SELECT "auth_user"."id" as "id",
             "auth_user"."username" as "username",
            ((COALESCE(MAX("submission_submission"."cases_passed"), 0)
            / GREATEST(COUNT(DISTINCT "test_case_testcasemodel"."id"), 1.0))
            * "problem_problem"."max_score") AS "score_temp"
            FROM "auth_user" LEFT OUTER JOIN "submission_submission"
            ON ("auth_user"."id" = "submission_submission"."user_id")
            LEFT OUTER JOIN "problem_problem"
            ON ("submission_submission"."problem_id" = "problem_problem"."id")
            LEFT OUTER JOIN "test_case_testcasemodel" ON
            ("problem_problem"."id" = "test_case_testcasemodel"."problem_id")
            GROUP BY
            "auth_user"."id",
            "submission_submission"."problem_id",
            "problem_problem"."max_score"
            ) as "querytable"
            LEFT OUTER JOIN "user_profile"
            ON ("user_profile"."user_id" = "querytable"."id")
            WHERE "user_profile"."rol" != 0
            GROUP BY
            "querytable"."id", "querytable"."username"
        '''
    )
    return scoreboard
