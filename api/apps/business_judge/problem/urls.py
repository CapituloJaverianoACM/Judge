from django.urls import path

from .views import (
    ProblemGeneralViewSet
)

urlpatterns = [
    path(
        'problems/',
        ProblemGeneralViewSet.as_view(),
        name='problems_general'
    )
]
