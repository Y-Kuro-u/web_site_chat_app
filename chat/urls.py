from django.urls import path
from chat.controller.lobby_controller.lobby_top import lobby_top
from chat.controller.room_controller.room_top import room_top
from chat.controller.room_controller.chat_text_in_room import chat_room
from chat.controller.model_controller.message_conteroller import get_text_ref_time

urlpatterns = [
    path('lobby', lobby_top, name='lobbies'),
    path("lobby/<int:lobby_id>/",room_top,name="rooms"),
    path("lobby/<int:lobby_id>/<int:room_id>/",chat_room,name="room"),
    path("api/",get_text_ref_time)
]