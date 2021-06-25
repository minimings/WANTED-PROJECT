from django.urls import path

from postings.views import MenuView, CompanyView

urlpatterns = [
    path('/menu', MenuView.as_view()),
    path('/company', CompanyView.as_view()),
]
