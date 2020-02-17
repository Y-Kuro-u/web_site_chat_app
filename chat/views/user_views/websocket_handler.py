from chat.models.messages import Message
from chat.models.users import User

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "-".join([self.scope["path"].split("/")
                                    [-3], self.scope["path"].split("/")[-2]])
        self.room_id = int(self.group_name.split("-")[-1])
        self.username = self.scope["user"].username
        self.display_name = User.objects.filter(
            username=self.username)[0].display_name

        async_to_sync(
            self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)

        self.accept()

    def disconnect(self, close_code):
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
            }
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(
            text_data=json.dumps(
                {"message": message,
                 "display_name": self.display_name
                 }
            )
        )
