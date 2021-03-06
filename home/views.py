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
        pins = request.POST['pin'].lower()
        phone = request.POST['phone'].lower()

        if re.match(r"[^@]+@[^@]+\.[^@]+", email) and (len(re.findall('[a-z]+', phone)) == 0 and len(re.findall('[a-z]+', pins)) == 0):
            pins = pins.split()
            for pin in pins:
                if len(pin) == 6:
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

                else:
                    return render(request, './index.html', {'form': CustomerForm(), 'flag': True})

            requests.post(
                "https://api.mailgun.net/v3/whenismyvaccine.in/messages",
                auth=(
                    "api", "83c8481eed353ca9d76bbdd3101a2b33-2a9a428a-5bb25d17"),
                data={"from": "When is my vaccine? <alerts@whenismyvaccine.in>",
                      "to": email,
                      "subject": "Thank for registering to WhenIsMyVaccine",
                      "text": f"Hello {email},\nThank you for registering to WhenIsMyVaccine!\n\nWe have received your request for alerts whenever vaccines get restocked in you area!\n You will be alerted for the pins: {pins}"})

            return render(request, './done.html')

        else:
            return render(request, './index.html', {'form': CustomerForm(), 'flag': True})

    return render(request, './index.html', {"form": CustomerForm(), 'flag': False})
