from django.db import models
from chat.models.lobbies import Lobby
from chat.models.users import User

class Room(models.Model):
    lobby_id = models.ForeignKey(Lobby,
                                 on_delete = models.CASCADE)
    
    user_ids = models.ManyToManyField(User)
    time_stamp = models.DateTimeField()