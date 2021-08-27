from django.db import models
from django.contrib.contenttypes.models import ContentType
from users.models import User

CHOICES = (('full', 'Full Time'), ('part', 'Part Time'), ('freelance', 'Freelance'))


class Work(models.Model):
    position = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    salary = models.CharField(max_length=30, blank=True)
    deadline = models.CharField(max_length=300, choices=CHOICES)
