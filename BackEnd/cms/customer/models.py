
from django.db import models


class customer(models.Model):
    First_Name = models.CharField(max_length=50, null=False, blank=False)
    Last_Name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    Address_Line1 = models.CharField(
        max_length=500, null=False, blank=False)
    Address_Line2 = models.CharField(max_length=500, null=True, blank=True)
    Phone_Number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name
