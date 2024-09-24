from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Location: '{self.name}' belongs to User: {self.user}"
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    quantity = quantity = models.IntegerField()
    storage_area = models.TextField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Item: '{self.name}' belongs to Location: {self.location}"