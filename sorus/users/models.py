from django.contrib.auth.models import AbstractUser
from django.db import models

from status.models import State


class UserType(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=100, null=False)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"UserType: id={self.id}, {self.description}"


class User(AbstractUser):
    notification_token = models.CharField(max_length=50)
    profile_image = models.TextField()
    user_type = models.ForeignKey(UserType, null=False, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.username}"

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=150, null=False)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)