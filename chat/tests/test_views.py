from django.test import TestCase, Client
from django.utils import timezone

from chat.models.users import User
from chat.models.rooms import Room
from chat.models.lobbies import Lobby


class UserViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test",
                                 password="test").save()

    def test_create_user(self):
        client = Client()
        response = client.post("/chat/signup/",
                               {"username": "create_test",
                                "user_password": "create_test",
                                "user_mailaddress": "create_test@gmail.com"
                                }
                               )
        self.assertEqual(response.status_code, 200)
        created_model = User.objects.filter(username="create_test")
        self.assertEqual(created_model[0].username, "create_test")

    def test_signin(self):
        client = Client()
        response = client.post("/chat/signin/",
                               {"username": "test",
                                "user_password": "test"
                                }
                               )
        self.assertEqual(response.status_code, 200)

    def test_signout(self):
        client = Client()
        client.login(username="test",
                     password="test"
                     )
        response = client.get("/chat/signout/")
        self.assertEqual(response.status_code, 200)


class LobbyViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test",
                                 password="test").save()

    def test_lobby_top_login(self):
        client = Client()
        client.login(username="test",
                     password="test"
                     )
        response = client.get("/chat/lobby/")
        self.assertEqual(response.status_code, 200)

    def test_lobby_top_not_login(self):
        client = Client()
        response = client.get("/chat/lobby/", follow=True)
        self.assertEqual(
            response.redirect_chain[0][0],
            "chat/signin?next=/chat/lobby/")


class RoomViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test",
                                 password="test").save()
        Lobby.objects.create(lobby_name="test_lobby").save()
        Room.objects.create(lobby_id=Lobby.objects.filter(lobby_name="test_lobby")[0],
                            room_name="test_room",
                            created_at=timezone.now()
                            ).save()

    def test_room_list_login(self):
        client = Client()
        client.login(username="test",
                     password="test"
                     )
        response = client.get("/chat/lobby/1/")
        self.assertEqual(response.status_code, 200)

    def test_lobby_top_login(self):
        client = Client()
        client.login(username="test",
                     password="test"
                     )
        response = client.get("/chat/lobby/1/1/")
        self.assertEqual(response.status_code, 200)

    def test_room_list_not_login(self):
        client = Client()
        response = client.get("/chat/lobby/1/")
        self.assertEqual(response.status_code, 302)

    def test_lobby_top_not_login(self):
        client = Client()
        response = client.get("/chat/lobby/1/1/")
        self.assertEqual(response.status_code, 302)
