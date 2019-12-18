from django.urls import path
from chat.views.Lobby_viewer.lobby_viewer import base_viewer as lobby_viewer
from chat.views.Room_viwer.room_viewr import base_viewer as room_viewr

urlpatterns = [
    path('lobby', lobby_viewer, name='lobby'),
    path("room/<int:lobby_id>/",room_viewr,name="room")
]