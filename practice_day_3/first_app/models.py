from django.db import models

# Create your models here.

class MakeModelForm(models.Model):
    # name = models.CharField(max_length=70,default="Dm")
    # roll = models.IntegerField(primary_key=True,default=1)
    # address = models.TextField(default="Dhaka")
    # father_name = models.TextField(default="Velox")
    # auto_field = models.AutoField(primary_key=True) 
    # big_auto_field = models.BigAutoField(primary_key=True)

    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    generic_ip_address_field = models.GenericIPAddressField()
    integer_field = models.IntegerField()
    url_field = models.URLField()

    

    # def __str__(self):
    #     return f"{self.name}"