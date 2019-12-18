from django.db import models
from chat.models.rooms import Room
from chat.models.users import User

class Message(models.Model):
    room_id = models.ForeignKey(Room,
                                on_delete = models.CASCADE)

    time_stamp = models.DateTimeField()
    user_id = models.OneToOneField(User,
                                   on_delete = models.CASCADE)