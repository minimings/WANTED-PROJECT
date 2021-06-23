from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('postings', include('postings.urls')),
    path('resumes', include('resumes.urls')),
    path('recommendations', include('recommendations.urls'))
]