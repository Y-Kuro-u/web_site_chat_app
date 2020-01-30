from django.contrib.auth import models as auth_models
from django.db import models


class User(auth_models.User):
    display_name = models.CharField(max_length=20)
