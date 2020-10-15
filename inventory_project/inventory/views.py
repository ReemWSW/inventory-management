from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'inventory\home.html')

def detial(request):
    return render(request, 'inventory\detail_inventory.html')

def insert(request):
    return render(request, 'inventory\insert_inventory.html')