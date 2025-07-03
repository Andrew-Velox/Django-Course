from django.db import models
from Brand.models import Car_Brand
from django.contrib.auth .models import User

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=3)
    brand = models.ForeignKey(Car_Brand, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='Car/media/uploads/',null=True,blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Commented By: {self.name}"
    
class Odred(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} Bought {self.car.name} Car"