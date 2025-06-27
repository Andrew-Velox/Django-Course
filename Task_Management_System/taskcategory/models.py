from django.db import models
from taskmodel.models import Task
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)
    task = models.ManyToManyField(Task)


    def __str__(self):
        return f"{self.name}"
