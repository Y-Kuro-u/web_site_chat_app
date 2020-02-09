from chat.views import lobby_views, room_views
from chat.views.user_views import user_controller

from django.urls import path

urlpatterns = [
    path('lobby', lobby_views.lobby_top, name='lobbies'),
    path("lobby/<int:lobby_id>/", room_views.room_list, name="rooms"),
    path("lobby/<int:lobby_id>/<int:room_id>/",
         room_views.chat_room, name="room"),
    path("signup", user_controller.create_user),
    path("signin", user_controller.login_user),
    path("signout", user_controller.logout_user)
]
