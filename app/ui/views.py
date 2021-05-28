from django.shortcuts import render
from django.views.generic import View

class LogIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/home")
        return render(request, "login.html")

    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/home")
        else:
            context = {
                "error": "User Not Found!"
            }
            return render(request, "login.html", context)
