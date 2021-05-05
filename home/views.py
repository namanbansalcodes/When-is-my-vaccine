from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
import re
import requests
# Create your views here.


def index(request):
    if request.method == 'POST':
        email = request.POST['email'].lower()
        pin = request.POST['pin'].lower()

        if len(pin) == 6:
            if len(re.findall('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email)) == True and len(re.findall('[a-z]+', pin)) == 0:

                if len(Customer.objects.filter(pin=pin)) != 0:
                    flag2 = Customer.objects.filter(pin=pin)[0].flag2
                else:
                    flag2 = 0

                user = Customer(
                    email=request.POST['email'],
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
