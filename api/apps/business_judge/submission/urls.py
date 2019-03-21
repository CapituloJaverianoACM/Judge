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
    ),
    path(
        'source_code/<int:id>/',
        SubmissionViewSet.as_view({
            'get': 'get_source_code'
        }),
        name='problem_single'
    )
]
