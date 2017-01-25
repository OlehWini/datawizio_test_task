from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.TextField(max_length=30)
    addres=models.TextField(max_length=30)
    open_date=models.DateTimeField()
