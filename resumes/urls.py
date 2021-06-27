from django.urls import path

from resumes.views import FileResumeView

urlpatterns = [
    path('/file', FileResumeView.as_view()),
    path('/file/<int:id>', FileResumeView.as_view())
]

