from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14)
    pin = models.IntegerField()


