from django.core.validators import MaxValueValidator
from django.db import models

from status.models import State
from users.models import User


class Product(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.FloatField(null=False)
    image = models.TextField(null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)
    promoter_id = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)


class Review(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(validators=[MaxValueValidator(5)])
    title = models.CharField(max_length=100)
    comment = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
