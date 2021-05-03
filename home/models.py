from django.db import models
import uuid
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(validators=[phone_regex],max_length=14)
    pin = models.IntegerField()


