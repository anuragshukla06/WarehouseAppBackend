from django.db import models

# Create your models here.
class warehouse(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class cropAndPrice(models.Model):
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE)
    crop = models.CharField(max_length=200)
    price = models.IntegerField()

class Detail(models.Model):
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE)
    detail = models.TextField(max_length=10000)