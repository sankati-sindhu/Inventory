from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    hireDate = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now = True)

    def __str__(self):
        return f"profile of {self.firstName}"
    
    
    