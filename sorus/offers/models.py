from datetime import datetime
from django.core.validators import MaxValueValidator
from django.db import models

from status.models import State
from users.models import User


class Category(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, blank=True)
    icon_name = models.CharField(max_length=50, null=False, blank=False)


class Product(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.FloatField(null=False)
    image = models.TextField(null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)
    promoter = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING)

    @property
    def time_left(self):
        ed = self.end_date.replace(tzinfo=None)
        time = ed - datetime.now()
        return time.days * 86_400 + time.seconds

    @property
    def still_active(self):
        return self.time_left > 0


class Review(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(validators=[MaxValueValidator(5)])
    title = models.CharField(max_length=100)
    comment = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    stars = models.IntegerField(default=0)
