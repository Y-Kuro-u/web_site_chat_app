from chat.models.rooms import Room
from chat.models.users import User
from django.db import models
from django.utils import timezone

class MessageManager(models.Manager):

    def store(self, text, room_id, username):
        Message(text=text,
                room_id=Room.objects.filter(id=room_id)[0],
                username=User.objects.filter(username=username)[0],
                created_at=timezone.now()).save()

class Message(models.Model):
    objects = MessageManager()

    room_id = models.ForeignKey(Room,
                                on_delete=models.CASCADE)

    created_at = models.DateTimeField()
    username = models.ForeignKey(User,
                                on_delete=models.CASCADE)

    text = models.CharField(max_length=1000)