from django.db import models
import datetime
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=70)
    task_des = models.TextField()
    is_complete = models.BooleanField(default=False)
    task_ass_date = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return f"{self.title}"
