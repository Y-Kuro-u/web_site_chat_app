from django.shortcuts import render
from chat.models.rooms import Room
from chat.models.messages import Message
from chat.controller.message_form import Message_form
from chat.controller.store_message import store_message
from django.template import loader
from django.http import HttpResponse

def base_viewer(request,lobby_id,room_id):
    if request.method == "POST":
        send_message = Message_form(request.POST)
        if send_message.is_valid():
            store_message(send_message,room_id)
        else:
            pass
        
    message_lists = Message.objects.filter(room_id = room_id)
    context = {"message_lists":message_lists,
               "form":Message_form}
    return render(request, "Room/room.html", context=context)