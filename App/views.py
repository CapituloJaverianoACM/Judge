from django.shortcuts import render

from App.views_class.log_view import LogViewSet
from App.views_class.user_view import UserViewSet
from App.views_class.auth_view import ObtainExpiringAuthToken
# Create your views here.



logs = LogViewSet.as_view(dict(get='list' , post='create'))
user = UserViewSet.as_view(dict(post='create'))
auth = ObtainExpiringAuthToken.as_view()


