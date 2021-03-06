from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Stock
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	form = 'Welcome This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "inventory/home.html",context)

def list_item(request):
	header = 'List of Items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}

	if request.method == 'POST':
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value()
										)
		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
	return render(request, "inventory/list_stock.html", context)

def add_item(request):
	title = "Add Item"
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_item')
	
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "inventory/add_stock.html", context)

def update_item(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_item')

	context = {
		'form':form
	}
	return render(request, 'inventory/add_stock.html', context)

def delete_item(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_item')
	return render(request, 'inventory/delete_item.html')