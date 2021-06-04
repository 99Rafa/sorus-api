from django.contrib.auth.models import AbstractUser
from django.db import models
from users.default_image import image

from status.models import State


class UserType(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=100, null=False)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"UserType: id={self.id}, {self.description}"


class Subscription(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    description = models.CharField(max_length=100, null=False)
    quantity_of_offers = models.IntegerField(null=False)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)


class User(AbstractUser):
    notification_token = models.CharField(max_length=50)
    profile_image = models.TextField(default=image)
    user_type = models.ForeignKey(
        UserType, null=False, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)
    address = models.TextField()
    stars = models.IntegerField(default=0)
    subscription = models.ForeignKey(
        Subscription, null=False, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return f"{self.username}"
