from django.urls import re_path
from chat.views.user_views.websocket_handler import ChatConsumer

websocket_url_patterns = [
    re_path(r"chat/lobby/[0-9]*/[0-9]*/$", ChatConsumer)
]
