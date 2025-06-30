from django.db import models
from categories.models import Categorie
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.ManyToManyField(Categorie) #many to many relation of post and categorie
    author = models.ForeignKey(User, on_delete=models.CASCADE) #One to Many relation of post and Author


    def __str__(self):
        return f"{self.title}"