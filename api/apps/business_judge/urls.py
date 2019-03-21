from django.urls import path, include

urlpatterns = [
    path('users/', include('business_judge.user.urls')),
    path('problems/', include('business_judge.problem.urls')),
    path('submissions/', include('business_judge.submission.urls')),
    path('test_cases/', include('business_judge.test_case.urls'))
]
