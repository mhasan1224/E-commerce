from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')