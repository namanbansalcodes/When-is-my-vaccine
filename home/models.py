from django.db import models
import uuid
from phone_field import PhoneField

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = PhoneField(blank=False)
    pin = models.IntegerField()


