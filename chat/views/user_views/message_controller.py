from django.utils import timezone
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from chat.models.messages import Message
from chat.models.rooms import Room
from chat.models.users import User


def store_message(text, room_id):
    Message(text=text,
            room_id=Room.objects.filter(id=room_id)[0],
            user_id=User.objects.filter(user_name="unknown")[0],
            time_stamp=timezone.now()).save()


@ensure_csrf_cookie
def get_text_ref_time(response, room_id, last_message_id):
    messages = Message.objects.filter(
        room_id=room_id).filter(
        id__gte=last_message_id)
    text_list = {message.id: message.text for message in messages}
    return JsonResponse(text_list)
