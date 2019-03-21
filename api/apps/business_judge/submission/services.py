from django.db.models.query import QuerySet

from .models import Submission
from business_judge.user.selectors import get_user_by_username
from business_judge.problem.selectors import get_problem_by_id
from .tasks import (
    judge_submission
)
from .selectors import (
    get_submission_by_id
)
from .constants import (
    VERDICT_CHOICES
)



def create_submission(
        *,
        user: str,
        problem: int,
        language: str,
        source_code,
        host_address: str
) -> Submission:

    submission = Submission.objects.create(
        user=get_user_by_username(username=user),
        problem=get_problem_by_id(id=problem),
        language=language,
        source_code=source_code
    )
    print("Send to queue")
    judge_submission.delay(
        submission.id,
        host_address
    )

    return submission

