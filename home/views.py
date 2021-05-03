from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        user = Customer(
            phone=request.POST['phone'],
            pin=request.POST['pin']
        )

        user.save()

        return render(request, './done.html')

    return render(request, './index.html', {"form": CustomerForm()})
