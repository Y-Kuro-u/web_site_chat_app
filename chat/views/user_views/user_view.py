from chat.models.users import User
from chat.views import lobby_view

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        user_mailaddress = request.POST.get("user_mailaddress", None)
        user_password = request.POST.get("user_password", None)

        if(username and user_password and user_mailaddress):
            user = User.objects.create_user(username,
                                            user_mailaddress,
                                            user_password)

            user.save()

        user_status = authenticate(request=request,
                                   username=username,
                                   password=user_password)

        if user_status is not None:
            login(request, user_status)

            return lobby_view.lobby_top(request)

    return render(request, "User/create_user.html")


def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username", None)
        user_password = request.POST.get("user_password", None)

        if(username and user_password):
            user_status = authenticate(request=request,
                                       username=username,
                                       password=user_password)

            if user_status is not None:
                login(request, user_status)

                return lobby_view.lobby_top(request)

        return lobby_view.lobby_top(request)

    return render(request, "User/login_user.html")


def logout_user(request):
    logout(request)

    return login_user(request)
