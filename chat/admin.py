from django.contrib import admin
from chat.models import *

admin.site.register(Lobby)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Message)