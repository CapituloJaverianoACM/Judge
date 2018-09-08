from App.log.view import LogViewSet
from App.user.view import UserViewSet
from App.auth.view import ObtainExpiringAuthToken
from App.problem.view import ProblemViewSet


logs = LogViewSet.as_view(dict(get='list', post='create'))
user = UserViewSet.as_view(dict(post='create'))
auth = ObtainExpiringAuthToken.as_view()
problem = ProblemViewSet.as_view(dict(post='create'))