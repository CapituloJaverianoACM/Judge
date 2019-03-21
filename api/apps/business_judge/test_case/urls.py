from django.urls import path

from .views import (
    TestCaseViewSet
)

urlpatterns = [
    path(
        'input/<int:id>/',
        TestCaseViewSet.as_view({
            'get':'get_input_by_id'
        }),
        name='get_input_by_id'
    ),
    path(
        'output/<int:id>/',
        TestCaseViewSet.as_view({
            'get':'get_output_by_id'
        }),
        name='get_output_by_id'
    )
]