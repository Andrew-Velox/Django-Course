from django.db import models
from categories.models import Categorie
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.ManyToManyField(Categorie) #many to many relation of post and categorie
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #One to Many relation of post and Author


    def __str__(self):
        return f"{self.title}"