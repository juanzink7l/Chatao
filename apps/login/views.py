from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):
    return render(request, "login.html")

def logout_view(request):
    auth_logout(request)
    return render(request, "registration/logged_out.html")