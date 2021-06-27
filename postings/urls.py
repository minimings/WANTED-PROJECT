from django.urls import path

from postings.views import MenuView, CompanyView, JobPostingView, CompanyListView

urlpatterns = [
    path('/menu', MenuView.as_view()),
    path('/company', CompanyView.as_view()),
    path('/job', JobPostingView.as_view()),
    path('/companylist', CompanyListView.as_view())
]