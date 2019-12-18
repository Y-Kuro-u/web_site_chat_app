from django.db import models
from chat.models.lobbies import Lobby
from chat.models.users import User

class Room(models.Model):
    lobby_id = models.ForeignKey(Lobby,
                                 on_delete = models.CASCADE)
    room_name = models.CharField(max_length=15)
    user_ids = models.ManyToManyField(User)
    time_stamp = models.DateTimeField()