from django.db import models

# Create your models here.
class cor(models.Model):
    origin=models.CharField(max_length=32)
    destination=models.CharField(max_length=32)
    marks=models.IntegerField()