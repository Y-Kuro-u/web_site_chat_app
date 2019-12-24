from chat.controller.model_controller import store_message

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "-".join([self.scope["path"].split("/")[-3],self.scope["path"].split("/")[-2]])
        self.room_id = int(self.group_name.split("-")[-1])
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.accept()

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)

    def receive(self,text_data):
        text_json = json.loads(text_data)
        print(text_json)
        message = text_json["message"]
        
        store_message.store_message(
            text = message,
            room_id = self.room_id
        )

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type":"chat_message",
                "message":message
            }
        )

    def chat_message(self,event):
        message = event["message"]
        self.send(
            text_data=json.dumps(
                {"message":message}
            )
        )