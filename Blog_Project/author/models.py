from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phn_number = models.CharField(max_length=12)

    def __str__(self):
        return f"Author: {self.name}"
