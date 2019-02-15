from django.urls import path


from .views import (
    UserViewSet,
    ScoreBoardViewSet
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
    ),
    path(
        'scoreboard/',
        ScoreBoardViewSet.as_view(
            {
                'get': 'get_all'
            }
        ),
        name='scoreboard'
    )
]
