from chat.models.lobbies import Lobby

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="chat/signin")
def lobby_top(request):
    lobby_lists = Lobby.objects.all()
    context = {"lobby_lists": lobby_lists}

    return render(request, "Lobby/lobby_lists.html", context=context)
