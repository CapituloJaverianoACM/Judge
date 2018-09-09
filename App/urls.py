from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('api/logs/', views.logs),
    path('api/user/', views.user),
    path('api/user/<int:id>/', views.user_single),
    path('api/user/admin', views.user_admin),
    path('api/login/', views.auth),
    path('api/problem/', views.problem),
    path('api/problem/<int:id>/', views.problem_single),
    path('api/problem/test_case/', views.test_case),
    # path('api/description/', views.description),
    path('api/submission/', views.submission),
    path('api/submission/user/<int:id>/', views.submission_user),
    path('api/submission/user/', views.submission_user_login),
    path('api/submission/problem/<int:id>/', views.submission_problem),
    path('api/comment/', views.comment),
    path('api/comment/<int:id>/', views.comment_problem),
]
