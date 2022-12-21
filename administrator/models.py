from django.db import models

# Create your models here.

# model for customer
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15)
    Country = models.CharField(max_length=50)
    Domains = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class Country(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name