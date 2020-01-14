from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from chat.views.user_viewer.user_info_viwer import user_create_viewer,login_viewer
from chat.controller.lobby_controller.lobby_top import lobby_top
    
def create_user(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name",None)
        user_mailaddress = request.POST.get("user_mailaddress",None)
        user_password = request.POST.get("user_password",None)

        if(user_name and user_password and user_mailaddress):
            user = User.objects.create_user(user_name,
                                            user_mailaddress,
                                            user_password)
            
            user.save()
        
        user_status = authenticate(request=request,
                                   username = user_name,
                                   password = user_password)
        
        if user_status is not None:
            login(request,user_status)
            return lobby_top(request)

    return user_create_viewer(request)

def login_user(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name",None)
        user_password = request.POST.get("user_password",None)
        if(user_name and user_password):
            user_status = authenticate(request=request,
                                       username=user_name,
                                       password=user_password)
            
            if user_status is not None:
                login(request,user_status)
                return lobby_top(request)
        
        print("error")
        return lobby_top(request)
    
    return login_viewer(request)
    

def logout_user(request):
    logout(request)
    return lobby_top(request)