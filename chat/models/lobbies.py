from django.db import models

class Lobby(models.Model):
    lobby_name = models.CharField(max_length=50)
    