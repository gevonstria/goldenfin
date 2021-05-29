from django.contrib import admin
from django.urls import path, include
from backend.views import LogIn, LoanDetails

urlpatterns = [
    path('login', LogIn.as_view()),
    path('loans', LoanDetails.as_view()),
]
