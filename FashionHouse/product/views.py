from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_details(request):
    return render(request, 'product_details.html')

def shop(request):
    return render(request, 'shop.html')