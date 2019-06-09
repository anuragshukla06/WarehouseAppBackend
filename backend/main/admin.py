from django.contrib import admin
from . import models

admin.site.register(models.warehouse)
admin.site.register(models.cropAndPrice)
admin.site.register(models.Detail)

# Register your models here.
