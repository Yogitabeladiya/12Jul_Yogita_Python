from django.db import models

# Create your models here.


class Book(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=10)
    publisher=models.CharField(max_length=50)