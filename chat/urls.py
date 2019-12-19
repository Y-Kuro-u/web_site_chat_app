from django.urls import path
from chat.views.Lobby_viewer.lobby_list_viewer import base_viewer as lobby_list_viewer
from chat.views.Room_viwer.room_list_viewr import base_viewer as room_list_viewr
from chat.views.Room_viwer.room_viewer import base_viewer as room_viewr

urlpatterns = [
    path('lobby', lobby_list_viewer, name='lobbies'),
    path("lobby/<int:lobby_id>/",room_list_viewr,name="rooms"),
    path("lobby/<int:lobby_id>/<int:room_id>/",room_viewr,name="room")
]