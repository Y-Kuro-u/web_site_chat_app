from chat.models.rooms import Room
from django.template import loader
from chat.views.Room_viwer.room_list_viewr import list_viewer

def room_top(request,lobby_id):
    room_lists = Room.objects.filter(lobby_id = lobby_id)
    context = {"room_lists":room_lists,
               "lobby_id":lobby_id}
               
    return list_viewer(request,context)