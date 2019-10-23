from django.shortcuts import render
# from generate import random_password

def index(request):
    return render(request, 'mainApp/homePage.html')

# def generation(request):
#         return random_password
