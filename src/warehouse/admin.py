from django.contrib import admin

from .models import Location, Warehouse
# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Location)