from django.db import models
from musician.models import Musician
import datetime
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=40)

    relase_date = models.DateField(default=datetime.date.today)
    
    RATINGS = [
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five'),
    ]
    raing = models.CharField(max_length=10,choices=RATINGS)

    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.album_name}"