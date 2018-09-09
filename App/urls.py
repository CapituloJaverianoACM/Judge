from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('api/logs/', views.logs),
    path('api/user/', views.user),
    path('api/login/', views.auth),
    path('api/problem/', views.problem),
    # path('api/description/', views.description),
    path('api/submission/', views.submission),
    path('api/comment/', views.comment),
]
