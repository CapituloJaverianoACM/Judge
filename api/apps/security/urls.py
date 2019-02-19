from django.urls import path
from .views import ObtainExpiringAuthToken


handler404 = 'views.page_not_found'

urlpatterns = [
    path(
        'login/',
        ObtainExpiringAuthToken.as_view({
            'get': 'get',
            'delete': 'delete',
            'post': 'post'
        }),
        name='auth'
    ),
]
