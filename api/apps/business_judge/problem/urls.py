from django.urls import path

from .views import (
    ProblemGeneralViewSet
)

urlpatterns = [
    path(
        '',
        ProblemGeneralViewSet.as_view({
            'get':'get'
        }),
        name='problems_general'
    )
]
