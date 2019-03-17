from .models import Submission
from business_judge.user.selectors import get_user_by_username
from business_judge.problem.selectors import get_problem_by_id
from .tasks import (
    judge_submission
)



def create_submission(
        *,
        user: str,
        problem: int,
        language: str,
        source_code
) -> Submission:

    submission = Submission.objects.create(
        user=get_user_by_username(username=user),
        problem=get_problem_by_id(id=problem),
        language=language,
        source_code=source_code
    )
    print("fhisdah")
    judge_submission.delay()
    print("2222")

    return submission
