from django.urls import path, include

urlpatterns = [
    path('user/', include('business_judge.users.urls')),
]
