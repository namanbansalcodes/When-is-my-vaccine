from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
import re
# Create your views here.


def index(request):
    if request.method == 'POST':
        phone = request.POST['phone'].lower()
        pin = request.POST['pin'].lower()

        if len(phone) == 10 and len(pin) == 6:
            if len(re.findall('[a-z]+', phone)) == 0 and len(re.findall('[a-z]+', pin)) == 0:

                if len(Customer.objects.filter(pin=pin)) != 0:
                    flag2 = Customer.objects.filter(pin=pin)[0].flag2
                else:
                    flag2 = 0

                user = Customer(
                    phone=request.POST['phone'],
                    pin=request.POST['pin'],
                    flag1=0,
                    flag2=flag2
                )

                user.save()

                return render(request, './done.html')

            else:
                pass
        else:
            pass

    return render(request, './index.html', {"form": CustomerForm()})
