from django.db import models
from django.core.validators import RegexValidator
from country_region_list import country_list
from django.core.exceptions import ObjectDoesNotExist

PHONE_REGEX = RegexValidator(
	regex=r'^\+?1?\d{9,15}$',
	message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)
EMAIL_REGEX = RegexValidator(
	regex=r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
	message = "Invalid Email"
)    



# Create your models here.
class Warehouse(models.Model):

	name = models.CharField(help_text = "If there is the name for the waore",blank = True, max_length=50, default="N\A")

	email = models.CharField(validators=[EMAIL_REGEX], help_text = "The email of the point of contact", max_length=254)

	phoneNo = models.CharField(validators=[PHONE_REGEX], verbose_name= ('Phone Number'), max_length = 17, help_text = "Ihe phone number of the point of contact")

	totalSpace = models.IntegerField(help_text = "The area of the warehouse in sq m", verbose_name=('Total Space'), default = 0)

	created =models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def Meta():
		ordering = ['updated']

	def delete(self, using=None):
		location = self.warehouse_location
		super().delete(using=using)
		print("$32")
		location.delete()

	def __str__(self):
		try:
			if self.name != "N\A":
				return 'Warehouse {0}, {1}'.format(self.warehouse_location.city,self.warehouse_location.region)
			else:
				return '{0} Warehouse {1}, {2}'.format(self.name,self.warehouse_location.city,self.warehouse_location.region)
		except:
			return f"{self.name} {self.created}"

class Location(models.Model):

	warehouse = models.OneToOneField("Warehouse", verbose_name=("Warehoues located in this location"), on_delete=models.CASCADE, blank=False)

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

	# def delete(self, using = None):
	# 	try:
	# 		# self.warehouse
	# 		# self.supplier
	# 		# self.order
	# 		print('CAnt delete warehoues exists' )
	# 	except ObjectDoesNotExist:
	# 		super().delete(using=using)
			
		

	def __str__(self):
		return 'Country code:{0} Area Code:{1} city: {2} pincode:{3}'.format(self.country, self.region, self.city, self.pincode)
