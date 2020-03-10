from chat.views import lobby_view, room_view, top_page_view
from chat.views.user_views import user_view

from django.urls import path

urlpatterns = [
    path("top/",top_page_view.top_page_view),
    path('lobby/', lobby_view.lobby_top, name='lobby'),
    path("lobby/<int:lobby_id>/", room_view.room_list, name="rooms"),
    path("lobby/<int:lobby_id>/<int:room_id>/",
         room_view.chat_room, name="room"),
    path("signup/", user_view.create_user, name="signup"),
    path("signin/", user_view.login_user, name="signin"),
    path("signout/", user_view.logout_user, name="signout")
]
