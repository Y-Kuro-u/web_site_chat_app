from django.urls import path
from chat.controller.lobby_controller.lobby_top import lobby_top
from chat.controller.room_controller.room_top import room_top
from chat.controller.room_controller.chat_text_in_room import chat_room
from chat.controller.model_controller.message_conteroller import get_text_ref_time
from chat.controller.model_controller.user_controller import create_user,login_user,logout_user

urlpatterns = [
    path('lobby', lobby_top, name='lobbies'),
    path("lobby/<int:lobby_id>/",room_top,name="rooms"),
    path("lobby/<int:lobby_id>/<int:room_id>/",chat_room,name="room"),
    path("api/",get_text_ref_time),
    path("signup",create_user),
    path("login",login_user),
    logout("logout",login_user)
]