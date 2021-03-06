from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=10,default='123456789')
    email = models.CharField(max_length=50,default='xuz@gmail.com')
    pin = models.IntegerField()
    flag1 = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)
