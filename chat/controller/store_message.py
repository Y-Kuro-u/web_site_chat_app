from django.utils import timezone
from chat.models.messages import Message
from chat.models.rooms import Room
from chat.models.users import User

def store_message(post_message,room_id):
    text_data = post_message.cleaned_data["text"]
    Message(text = text_data,
            room_id = Room.objects.filter(id = room_id)[0],
            user_id = User.objects.filter(user_name = "unknown")[0],
            time_stamp = timezone.now()).save()