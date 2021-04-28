from django.db import models
from supplier.models import Supplier
from warehouse.models import Warehouse
from uuid import uuid4
from django.shortcuts import reverse
# Create your models here.


#Item model 
class Item(models.Model):
	itemCode = models.CharField(
		max_length=8,
		blank = True,
		primary_key = True,
		default=""
	)

	#the item name
	name = models.CharField(max_length = 200, help_text="Enter the item name")

	#description of the item
	description = models.TextField(max_length = 500, help_text="Features of the items")

	#Image of the item if uploaded or it takse as the default
	itemImg = models.ImageField(upload_to='item', default="no_image.jpeg")

	#stores the created date
	created = models.DateTimeField(auto_now_add=True)

	#stores the latest updated date
	updated = models.DateTimeField(auto_now=True)

	#all the suppliers for the item, each supplier can have supply multiple items, and each item can have multiple suppliers
	# suppliers = models.ManyToManyField(Supplier)

	def save(self):
		if self.itemCode == "":
			self.itemCode = str(uuid4()).replace('-', '').upper()[:8]
		super().save(self)


	class Meta:
		ordering = ['name']
	
	def get_absolute_url(self):
		return reverse("item:detail", kwargs={'pk':  self.pk})
	
	def __str__(self):
		return self.name


class ItemSuppliers(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)
	item = models.ForeignKey('Item', on_delete = models.CASCADE)
	# itemInstances = models.ForeignKey('ItemInstance', on_delete = models.CASCADE, null=True)

	def save(self):
		if not ItemSuppliers.objects.filter(supplier = self.supplier, item = self.item).exists():
			super().save(self)

	def __str__(self):
		return f"{self.item} {self.supplier.name} "
	
	def get_absolute_url(self):
		return reverse("model_detail", kwargs={"pk": self.pk})
	


# #Item instance
class ItemInstance(models.Model):
	itemId = models.UUIDField(
		unique = True,
		primary_key = True,
		default = uuid4,
		help_text="Example: c8daa3ac-3dd0-44e9-ba2a-b0cbd1c8d8ae.",
	)

	itemsup = models.ForeignKey('ItemSuppliers', on_delete = models.CASCADE, null=True)
	# item = models.OneToOneField('Item', on_delete = models.CASCADE)
	# #Item name 
	# supplier = models.OneToOneField(Supplier, on_delete = models.CASCADE)
	manufatured = models.DateField()
	ITEM_STATUS = (
		('a', 'Available'),
		('d', 'defecitve'),
		('r', 'returned'),
		('e', 'defective/expired'),
		('s', 'sold')
	)
	status = models.CharField(
		choices=ITEM_STATUS,
		default='a',
		max_length=1
	)

	# def __str__(self):
	# 	return f"{self.item} {self.itemId}"
	

	
