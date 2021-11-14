from django.db import models
from django.utils import timezone

# Create your models here.

class TodoList(models.Model): 
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.CharField(max_length=100, default="general")
    def __str__(self):
        return self.title