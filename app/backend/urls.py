from django.contrib import admin
from django.urls import path, include
from backend.views import LogIn

urlpatterns = [
    path('login', LogIn.as_view()),
]
