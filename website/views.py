from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')
def celebrate(request):
    return render(request,'celebrate_birthday.html')
