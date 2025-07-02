from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phn_number = models.CharField(max_length=12)
    instrument_type = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"