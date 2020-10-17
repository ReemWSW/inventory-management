from django.shortcuts import render
from django.http import HttpResponse

from .models import Stock
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "inventory\home.html",context)

def detial(request):
    return render(request, 'inventory\detail_inventory.html')
    
def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "inventory\list_stock.html", context)