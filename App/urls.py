from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
    path('logs/', views.logs),
    path('user/', views.user),
    path('login/', views.auth),
]
