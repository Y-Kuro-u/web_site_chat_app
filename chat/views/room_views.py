from chat.models.rooms import Room
from chat.models.messages import Message
from chat.views.user_views import message_form
from chat.views.user_views.message_conteroller import store_message

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def chat_room(request, lobby_id, room_id):
    if request.method == "POST":
        send_message = Message_form(request.POST)
        if send_message.is_valid():
            store_message(send_message, room_id)
        else:
            pass

    message_lists = Message.objects.filter(room_id=room_id)
    context = {"message_lists": message_lists,
               "form": message_form}

    return render(request, "Room/room.html", context=context)


def room_list(request, lobby_id):
    room_lists = Room.objects.filter(lobby_id=lobby_id)
    context = {"room_lists": room_lists,
               "lobby_id": lobby_id}

    return render(request, "Room/room_lists.html", context=context)
