from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import View
from django.http import JsonResponse
import json

class LogIn(View):
    def post(self, request):
        post_data = json.loads(request.body)
        user = authenticate(username=post_data["username"], password=post_data["password"])
        if user is not None:
            message = "valid"
        else:
            message = "invalid"
            # No backend authenticated the credentials
        return JsonResponse({"message": message})

