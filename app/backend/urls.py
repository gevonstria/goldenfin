from django.contrib import admin
from django.urls import path, include
from backend.views import LogIn, Loan, LoanDescribe

urlpatterns = [
    path('login', LogIn.as_view()),
    path('loans', Loan.as_view()),
    path('loan/<loan_id>', LoanDescribe.as_view())
]
