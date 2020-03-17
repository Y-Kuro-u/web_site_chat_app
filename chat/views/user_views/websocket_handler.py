from chat.models.messages import Message
from chat.models.users import User
from chat.models.rooms import Room

from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import redirect
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "-".join([self.scope["path"].split("/")
                                    [-3], self.scope["path"].split("/")[-2]])
        self.lobby_id = int(self.group_name.split("-")[-1])
        self.room_id = int(self.group_name.split("-")[-1])
        self.username = self.scope["user"].username
        self.display_name = User.objects.filter(username=self.username)[0].display_name

        self.user = User.objects.filter(username=self.username)[0]
        self.room = Room.objects.filter(pk=self.room_id)[0]
        self.room.user_ids.add(self.user)


        async_to_sync(
            self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        self.room.user_ids.remove(self.user)
        if self.room.user_ids.count() == 0:
            Room.objects.filter(pk=self.room_id)[0].delete()

        async_to_sync(
            self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name)

    def receive(self, text_data):
        text_json = json.loads(text_data)
        message = text_json["message"]

        Message.objects.store(text=text_data,
                              room_id=self.room_id,
                              username=self.username,
                              )
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat.message",
                "message": message,
                "username": self.username,
            }
        )

    def chat_message(self, event):
        message = event["message"]
        if event["username"] != self.username:
            self.send(
                text_data=json.dumps(
                    {"message": message,
                     "display_name": self.display_name
                     }
                )
            )
