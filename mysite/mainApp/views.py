from django.shortcuts import render
from mainApp.generate import random_password



def index(request):
    return render(request, 'mainApp/generator.html', {"random_password": random_password(), "Name": "Home"})
