from django.db import models

from offers.models import Product
from status.models import State
from users.models import User


class BuyMethod(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    description = models.CharField(max_length=150)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)


class Sale(models.Model):
    id = models.IntegerField(serialize=True, primary_key=True)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    buy_method = models.ForeignKey(BuyMethod, on_delete=models.DO_NOTHING)
    buy_date = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=36, null=False, blank=False)
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
