from django.db import models

# Create your models here.
class Lenguage(models.Model):
    name = models.CharField(max_length=10)
    
class Framework(models.Model):
    name = models.CharField(max_length=10)
    lenguage = models.ForeignKey(Lenguage, on_delete=models.CASCADE)