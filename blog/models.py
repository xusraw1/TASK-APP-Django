from django.db import models


# Create your models here.

class Task(models.Model):
    """Create Task Table in BD"""
    title = models.CharField('Task-name', max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title