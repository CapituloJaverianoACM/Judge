from App.log.view import LogViewSet
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken
from App.problem.view import ProblemViewSet
from App.description.view import DescriptionViewSet, TestCasesViewSet
from App.submission.view import SubmissionViewSet
from App.comment.view import CommmentViewSet

logs = LogViewSet.as_view(dict(get='list', post='create'))
user = UserViewSet.as_view(dict(post='create'))
auth = ObtainExpiringAuthToken.as_view()
problem = ProblemViewSet.as_view(dict(post='create', get='get'))
# description = DescriptionViewSet.as_view(dict())
submission = SubmissionViewSet.as_view(dict(post='create'))
comment = CommmentViewSet.as_view(dict(post='create'))
user_admin = UserViewSet.as_view(dict(delete='delete_by_id'))
user_single = UserViewSet.as_view(dict(get='get_by_id'))
submission_user = SubmissionViewSet.as_view(dict(get='get_by_user'))
submission_problem = SubmissionViewSet.as_view(dict(get='get_by_problem'))
problem_single = ProblemViewSet.as_view(dict(get='get_by_id'))
comment_problem = CommmentViewSet.as_view(dict(get='get'))
test_case = TestCasesViewSet.as_view(dict(post='create'))
submission_user_login = SubmissionViewSet.as_view(dict(get='get_sub_login'))