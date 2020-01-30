from django.db import models
from chat.models.rooms import Room
from chat.models.users import User


class Message(models.Model):
    room_id = models.ForeignKey(Room,
                                on_delete=models.CASCADE)

    created_at = models.DateTimeField()
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE)

    text = models.CharField(max_length=1000)
