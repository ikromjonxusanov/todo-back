from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model): 
    text = models.CharField(max_length=255)
    day = models.CharField(max_length=100)
    reminder = models.BooleanField(default=False)
    def __str__(self):
        return self.text