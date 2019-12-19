from django.shortcuts import render
from chat.models.rooms import Room
from chat.models.messages import Message
from django.template import loader
from django.http import HttpResponse

def base_viewer(request,lobby_id,room_id):
    message_lists = Message.objects.filter(room_id = room_id)
    context = {"message_lists":message_lists}
    return render(request, "Room/room.html", context=context)