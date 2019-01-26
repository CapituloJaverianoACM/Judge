from django.urls import path

from .views import (
    UserViewSet
)

urlpatterns = [
    path(
        'singup/',
        UserViewSet.as_view(
            {
                'post': 'post'
            }
        ),
        name='singup'
    )
]
