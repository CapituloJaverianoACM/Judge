from django.urls import path

from .views import (
    SubmissionViewSet
)

urlpatterns = [
    path(
        '',
        SubmissionViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='submissions'
    )
]
