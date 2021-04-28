from django.db import models
from item.models import Item
from warehouse.models import Warehouse
from country_region_list import country_list

# Create your models here.


class Order(models.Model):
	orderedItem = models.OneToOneField(Item, on_delete=models.CASCADE)
	orderDate = models.DateTimeField(auto_now_add=True)
	qty = models.DecimalField(decimal_places = 0, max_digits=10, default=1)
	expectedDeliveryDate = models.DateField()
	ORDER_STATUS = (
		('o', 'Order Placed'),
		('a', 'Assigned'),
		('d', 'Dispatched'),
		('c', 'Cancelled'),
		('f', 'Completed')
	)
	status = models.CharField(
		choices=ORDER_STATUS,
		default='o',
		max_length=1
	)

	# assignedWarehouse = models.OneToOneField(Warehouse, on_delete = models.CASCADE, blank=True)

	def __str__(self):
		return "{0}:{1} / {2}".format(self.item, self.qty, self.status)
	# def save(self):
	# 	if Warehoues.objects.filter(Country = self.deliverAddress.Country,  = 



class DeliveryAddress(models.Model):

	orderId =  models.OneToOneField('Order', verbose_name=('Order'), help_text="The order to be delivered to this address",on_delete=models.CASCADE, blank=False)

	billerName = models.CharField(max_length=120,verbose_name="Billers Name")

	COUNTRIES = country_list.all_countries()

	country = models.CharField(
		max_length = 3, 
		choices=COUNTRIES,
		blank=True,
		default='IN',
		help_text = 'Country'
	)

	REGIONS = country_list.all_regions()
	region = models.CharField(
		max_length = 10,
		choices = REGIONS,
		blank=True,
		help_text = 'Region',
		default = 'IN-AP'
	)

	city = models.CharField( max_length = 200, help_text = 'City')

	localAdress = models.TextField(max_length = 300, help_text = 'Breif description of the address')

	pincode = models.CharField( max_length = 12, help_text = 'Please enter the pincode according to the country you are in, for eg: Inida has 6 digits in pincode')
