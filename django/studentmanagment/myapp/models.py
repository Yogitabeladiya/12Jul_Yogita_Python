from django.db import models

# Create your models here.


class student(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)