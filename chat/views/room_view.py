from chat.models.rooms import Room
from chat.models.messages import Message
from chat.models.lobbies import Lobby

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url="chat/signin")
def chat_room(request, lobby_id, room_id):
    if Room.objects.filter(pk=room_id):

        message_lists = Message.objects.filter(room_id=room_id)
        context = {"message_lists": message_lists}

        return render(request, "Room/room.html", context=context)
    else:
        return redirect("/chat/lobby/{}/".format(lobby_id))


@login_required(login_url="chat/signin")
def room_list(request, lobby_id):

    room_lists = Room.objects.filter(lobby_id=lobby_id)
    context = {"room_lists": room_lists,
               "lobby_id": lobby_id}

    return render(request, "Room/room_lists.html", context=context)


@login_required(login_url="chat/signin")
def create_room(request, lobby_id):
    if request.method == "POST":
        create_room_name = request.POST.get("room_name", None)

        new_room = Room.objects.create(
            lobby_id=Lobby.objects.filter(id=lobby_id)[0],
            room_name=create_room_name,
            created_at=timezone.now()
        )
        new_room.save()

        room_id = new_room.id

        return redirect("/chat/lobby/{}/{}/".format(lobby_id, room_id))

    else:

        return render(request, "Room/create_room.html")
