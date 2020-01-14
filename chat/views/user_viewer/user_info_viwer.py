from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

def user_create_viewer(request):
    return render(request, "User/create_user.html")

def login_viewer(request):
    return render(request,"User/login_user.html")