from django.urls import re_path
from chat.controller.model_controller.websocket_hundler import ChatConsumer

websocket_url_patterns = [
    re_path(r"chat/lobby/[0-9]*/[0-9]*/$",ChatConsumer)
]