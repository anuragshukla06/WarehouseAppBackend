from django.db import models

# Create your models here.
class warehouse(models.Model):
    name = models.CharField(max_length=200)
    pricePerHour = models.IntegerField()
    area = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # TODO: Add a thumbnail
