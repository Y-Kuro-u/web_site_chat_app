from chat.views.Lobby_viewer import lobby_list_viewer
from django.shortcuts import render
from chat.models.lobbies import Lobby
from django.template import loader

def lobby_top(request):
    lobby_lists = Lobby.objects.all()
    context = {"lobby_lists":lobby_lists}

    return lobby_list_viewer.base_viewer(request,context)