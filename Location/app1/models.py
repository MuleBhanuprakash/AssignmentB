from django.db import models


# Create your models here.


class Address(models.Model):
    Name = models.CharField(max_length=30)
    Job = models.CharField(max_length=30)
    Address1 = models.CharField(max_length=30)
    Address2 = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Pinode = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.Name

    def full_address(self):
        return self.Address1, self.Address2, self.Area, self.City, self.Country, self.Pinode
