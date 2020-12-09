from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=250)
    dec = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    duration = models.IntegerField(max_length=250)

    def __str__(self):
        return self.name

class Tickets(models.Model):
    name = models.ForeignKey(Movies, on_delete=models.CASCADE)
    timing = models.DateTimeField(max_length=250)
    price = models.PositiveIntegerField(max_length=250)
    total_tickets = models.PositiveIntegerField(max_length=250)
    
    def __str__(self):
        return self.name+'-'+self.price
