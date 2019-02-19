from django.urls import path

from .views import (
    ProblemGeneralViewSet,
    ProblemSingleViewSet
)

urlpatterns = [
    path(
        '',
        ProblemGeneralViewSet.as_view({
            'get': 'get'
        }),
        name='problems_general'
    ),
    path(
        '<int:id>/',
        ProblemSingleViewSet.as_view({
            'get': 'get'
        }),
        name='problem_single'
    )
]
