from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

def base_viewer(request,context):
    return render(request, "Room/room.html", context=context)