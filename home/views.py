from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from .Templates import *

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        user = User(
            phone=request.POST['Phone'],
            pin=request.POST['pin']
        )

        user.save()

        return render(request, './home.done.html')

    return render(request, './home/index.html ', {"form": UserForm()})
