from django.db import models

# Create your models here.

# countries list
class Country(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

# model for customer
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15)
    Country = models.CharField(max_length=50)
    Domains = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

# model for domain
class Domain(models.Model):
    Customer_Name = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Domain_Name = models.CharField(max_length=50)
    Purchase_Date = models.DateField()
    Renewal_Date = models.DateField(null=True,blank=True)
    Amount = models.IntegerField(default=100)

    def __str__(self):
        return self.Domain_Name