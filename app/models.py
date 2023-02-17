from django.db import models

# Create your models here.
class Customer(models.Model):
    CID=models.IntegerField()
    Name=models.CharField(max_length=100)
    Locality=models.CharField(max_length=50)
    Description=models.TextField()
    def __str__(self):
        return self.Name