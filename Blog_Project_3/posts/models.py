from django.db import models
from categories.models import Categorie
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.ManyToManyField(Categorie) #many to many relation of post and categorie
    author = models.ForeignKey(User, on_delete=models.CASCADE) #One to Many relation of post and Author
    image =  models.ImageField(upload_to='posts/media/uploads/',null=True,blank=True)
    # file =  models.FileField(upload_to='posts/media/uploads/',null=True,blank=True)


    def __str__(self):
        return f"{self.title}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name = "comments")
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comments by: {self.name}"