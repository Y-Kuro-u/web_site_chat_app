from chat.models.users import User
from chat.views import lobby_views

from django.contrib.auth import authenticate, login, logout



def create_user(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name", None)
        user_mailaddress = request.POST.get("user_mailaddress", None)
        user_password = request.POST.get("user_password", None)

        if(user_name and user_password and user_mailaddress):
            user = User.objects.create_user(user_name,
                                            user_mailaddress, user_password)

            user.save()

        user_status = authenticate(request=request,
                                   username=user_name,
                                   password=user_password)

        if user_status is not None:
            login(request, user_status)

            return lobby_top(request)

    return render(request, "User/create_user.html")


def login_user(request):

    if request.method == "POST":
        user_name = request.POST.get("user_name", None)
        user_password = request.POST.get("user_password", None)

        if(user_name and user_password):
            user_status = authenticate(request=request,
                                       username=user_name,
                                       password=user_password)
            if user_status is not None:
                login(request, user_status)

                return lobby_top(request)

        return lobby_top(request)

    return render(request, "User/login_user.html")


def logout_user(request):
    logout(request)

    return lobby_views.lobby_top(request)
