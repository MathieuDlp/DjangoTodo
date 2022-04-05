from email.policy import default
from django.db import models
from django.forms import BooleanField, DateField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title