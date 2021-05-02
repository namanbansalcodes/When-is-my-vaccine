from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        user = User(
            phone=request.POST['Phone'],
            pin=request.POST['pin']
        )

        user.save()

        return render(request, './done.html')

    return render(request, './index.html ', {"form": UserForm()})
