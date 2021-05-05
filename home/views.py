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
        phone = request.POST['phone'].lower()

        if len(phone) == 10 and len(pin) == 6:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and (len(re.findall('[a-z]+', pin)) == 0 and len(re.findall('[a-z]+', phone)) == 0):

                if len(Customer.objects.filter(pin=pin)) != 0:
                    flag2 = Customer.objects.filter(pin=pin)[0].flag2
                else:
                    flag2 = 0

                user = Customer(
                    email=email,
                    phone=phone,
                    pin=pin,
                    flag1=0,
                    flag2=flag2
                )

                user.save()

                requests.post(
                    "https://api.mailgun.net/v3/sandbox8d2f3b59dbeb4627bc07e28a3284f960.mailgun.org/messages",
                    auth=("api", "83c8481eed353ca9d76bbdd3101a2b33-2a9a428a-5bb25d17"),
                    data={"from": "When is my vaccine? <alerts@whenismyvaccine.in>",
                          "to": email,
                          "subject": "Thank for registering to WhenIsMyVaccine",
                          "text": f"Hello {email},\nThank you for registering to WhenISMyVaccine!\n\nWe have reveived your request to receive alerts whenever vaccines get restocked in you area!\n You have registerd for the alerts for the pin: {pin}"})

                return render(request, './done.html')

            else:
                print('fail2')
        else:
            print('fail1')

    return render(request, './index.html', {"form": CustomerForm()})
