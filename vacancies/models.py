from django.db import models
from django.contrib.contenttypes.models import ContentType
from users.models import User

CHOICES = (('full', 'Full Time'), ('part', 'Part Time'), ('freelance', 'Freelance'))

class Work(models.Model):
    Position = models.CharField(max_length=30, blank=True)
    Location = models.CharField(max_length=30, blank=True)
    Salary = models.CharField(max_length=30, blank=True)
    Deadline = models.CharField(max_length=300, choices=CHOICES)
