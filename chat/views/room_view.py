from chat.models.rooms import Room
from chat.models.messages import Message

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="chat/signin")
def chat_room(request, lobby_id, room_id):
    message_lists = Message.objects.filter(room_id=room_id)
    context = {"message_lists": message_lists}

    return render(request, "Room/room.html", context=context)


@login_required(login_url="chat/signin")
def room_list(request, lobby_id):

    room_lists = Room.objects.filter(lobby_id=lobby_id)
    context = {"room_lists": room_lists,
               "lobby_id": lobby_id}

    return render(request, "Room/room_lists.html", context=context)
