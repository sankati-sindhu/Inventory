from django.contrib import admin
from .models import Item, ItemInstance, ItemSuppliers
# Register your models here.
admin.site.register(Item)
admin.site.register(ItemInstance)
admin.site.register(ItemSuppliers)