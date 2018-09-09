from App.log.view import LogViewSet
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken
from App.problem.view import ProblemViewSet
from App.description.view import DescriptionViewSet
from App.submission.view import SubmissionViewSet
from App.comment.view import CommmentViewSet

logs = LogViewSet.as_view(dict(get='list', post='create'))
user = UserViewSet.as_view(dict(post='create'))
auth = ObtainExpiringAuthToken.as_view()
problem = ProblemViewSet.as_view(dict(post='create'))
# description = DescriptionViewSet.as_view(dict())
submission = SubmissionViewSet.as_view(dict(post='create'))
comment = CommmentViewSet.as_view(dict(post='create'))
