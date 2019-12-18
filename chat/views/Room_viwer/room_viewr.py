from django.shortcuts import render
from chat.models.rooms import Room
from django.template import loader
from django.http import HttpResponse

def base_viewer(request,lobby_id):
    room_lists = Room.objects.filter(lobby_id = lobby_id)
    context = {"room_lists":room_lists}

    return render(request, "Room/room_base.html", context=context)