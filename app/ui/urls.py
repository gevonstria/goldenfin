from django.contrib import admin
from django.urls import path, include
from ui.views import Dashboard

urlpatterns = [
    path('dashboard', Dashboard.as_view()),
]
