from django.contrib.auth.models import User
from django.db import models

class State(models.Model):
    """An extension of user model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.CharField(blank=True, null=True, max_length=100)
    timestamp = models.IntegerField(blank=True, null=True)
