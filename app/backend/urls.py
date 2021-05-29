from django.contrib import admin
from django.urls import path, include
from backend.views import LogIn, Loan

urlpatterns = [
    path('login', LogIn.as_view()),
    path('loans', Loan.as_view()),
]
