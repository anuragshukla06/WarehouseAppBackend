from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

# Create your views here.
def home(request):
    return HttpResponse("Success")

def search(request, area, fruit, days):
    area = area.lower()
    warehouses = models.warehouse.objects.filter(area=area)
    arr = []
    for i in warehouses:
        dicti = {}
        dicti['name'] = i.name
        dicti['area'] = i.area
        dicti['pricePerHour'] = i.pricePerHour
        dicti['address'] = i.address
        arr.append(dicti)

    return HttpResponse(json.dumps(arr))

