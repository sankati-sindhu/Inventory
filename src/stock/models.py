from django.db import models
from item.models import ItemInstance 
from item.models import Warehouse
# Create your models here.

class warehouse_items(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, unique=False)
    itemInstance = models.OneToOneField(ItemInstance, on_delete=models.CASCADE)



class stock_items(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, unique=False)
    itemInstance = models.OneToOneField(ItemInstance, on_delete=models.CASCADE)
