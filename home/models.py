import email
from unittest.util import _MAX_LENGTH
from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class MechanicService(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    

    def __str__(self):
        return self.name

    
class CarServices(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    

    def __str__(self):
        return self.name

class DriverBookingCar(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    

    def __str__(self):
        return self.name

class CarBooking(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    model = models.CharField(max_length=50)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    pickdate = models.DateField(null=True)
    pickuptime = models.TimeField(null=True)
    dropdate = models.DateField(null=True)
    droptime = models.TimeField(null=True)
    

    def __str__(self):
        return self.name

class RentCar(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    model = models.CharField(max_length=50)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    pickdate = models.DateField(null=True)
    pickuptime = models.TimeField(null=True)
    dropdate = models.DateField(null=True)
    droptime = models.TimeField(null=True)
    

    def __str__(self):
        return self.name
