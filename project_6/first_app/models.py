from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=70)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="Velox")

    def __str__(self):
        return f"Name: {self.name} | Roll: {self.roll} | Address: {self.address} | Father: {self.father_name}"