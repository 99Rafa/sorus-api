from django.db import models


class State(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    description = models.CharField(max_length=100)
