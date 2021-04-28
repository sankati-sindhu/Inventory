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

class Supplier(models.Model):
	name = models.CharField(help_text = "Supplier Name", max_length=50, default="N\A")
	phoneNo = models.CharField(validators=[PHONE_REGEX], max_length = 17, help_text = "Ihe phone number of the point of contact")
	email = models.CharField(validators=[EMAIL_REGEX], help_text = "The email of the point of contact", max_length=254)
	# items = models.ManyToManyField(Item)
	def __str__(self):
		return "{0}".format(self.name)


class Location(models.Model):

	supplier = models.OneToOneField("Supplier", verbose_name=("Supplier located in this location"), on_delete=models.CASCADE, blank=False)

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
