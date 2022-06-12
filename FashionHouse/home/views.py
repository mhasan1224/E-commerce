from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=fname, last_name=lname)
        user.save()
        return redirect('/')
    return render(request, 'signup.html')


def Login(request):
    if request.method == 'POST':
        username = username.POST['username']
        password = password.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.warning(request, 'Please signup or account invalid')
        return render(request, 'login.html')
    return render(request, 'login.html')
