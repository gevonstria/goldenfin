from django.shortcuts import render
from django.views.generic import View

class LogIn(View):
    def get(self, request):
        return render(request, "login.html")

class Dashboard(View):
    def get(self, request):
        return render(request, "dashboard.html")