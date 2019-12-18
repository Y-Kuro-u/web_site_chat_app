from django.db import models

class Lobby(models.Model):
    name = models.CharField(max_length=50)
    