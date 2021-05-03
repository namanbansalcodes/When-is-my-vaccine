from django.db import models
import uuid
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True) # validators should be a list
    pin = models.IntegerField()


