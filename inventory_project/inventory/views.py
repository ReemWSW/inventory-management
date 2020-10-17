from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Stock
from .forms import StockCreateForm
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "inventory/home.html",context)

def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "inventory/list_stock.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_item')
    
    context = {
		"form": form,
		"title": "Add Item",
	}
    return render(request, "inventory/add_stock.html", context)