from django.shortcuts import render
from chat.models.rooms import Room
from django.template import loader
from django.http import HttpResponse

def list_viewer(request,context):
    return render(request, "Room/room_lists.html", context=context)