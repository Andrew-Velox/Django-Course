from django.shortcuts import render
from posts.models import Post
from categories.models import Categorie


def home(request, category_slug=None):
    data = Post.objects.all()

    if category_slug is not None:
        categories = Categorie.objects.get(slug = category_slug)
        data = Post.objects.filter(category = categories)
    categories = Categorie.objects.all()
    # print(data)
    return render(request,"home.html",{'data':data, 'categories':categories})