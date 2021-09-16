from django.db import models
from users.models import User

class Group(models.Model):
    choices = models.ManyToManyField(User)
