from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

# Create your views here.
def home(request):
    return HttpResponse("Success")

def search(request, area, crop, days):
    area = area.lower()
    crops = models.cropAndPrice.objects.filter(crop=crop)
    arr = []
    for i in crops:
        if i.warehouse.area == area:
            dicti = {}
            dicti['id'] = i.warehouse.id
            dicti['name'] = i.warehouse.name
            dicti['area'] = i.warehouse.area
            dicti['pricePerHour'] = i.price
            dicti['address'] = i.warehouse.address
            arr.append(dicti)

    return HttpResponse(json.dumps(arr))

def detail(request, id):
    warehouse = models.warehouse.objects.get(id=id)
    detail = models.Detail.objects.get(warehouse=warehouse)

    return HttpResponse(detail.detail)