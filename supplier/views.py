from django.shortcuts import render, redirect,get_object_or_404
import datetime as dt
from .models import *
from .forms import *

from sales.models import *

def all_suppliers(request):
    suppliers = Supplier.objects.all()
    total_suppliers = Supplier.objects.all().count()
    return render(request, 'supplier/manage_supplier.html', locals())

def add_item(request, cls):
        
    if request.method == "POST":
        form = cls(request.POST)


        if form.is_valid():
            form.save()
            return redirect('all_suppliers')

    else:
        form = cls()
        return render(request, 'add_new_supplier.html', locals())



def add_supplier(request):
    return add_item(request, SupplierForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('all_suppliers')
    else:
        form = cls(instance=item)

        return render(request, 'edit_supplier.html', locals())

def edit_supplier(request, pk):
    return edit_item(request, pk, Supplier, SupplierForm)

def delete_supplier(request, pk):

    template = 'supplier/manage_supplier.html'
    Supplier.objects.filter(id=pk).delete()
    suppliers = Supplier.objects.all()
    
    return render(request, template, locals())


def purchase_report(request):
    purchases = Supplier.objects.all()
    total = [i.materials.price * i.materials.quantity for i in purchases]
    final_total = sum(total)
   
    return render(request, 'reports/purchase_report.html', locals())

def todays_purchase(request):
        date = dt.date.today()
        purchases = Supplier.todays_purchase()
        total_purchase = [i.materials.price * i.materials.quantity for i in purchases]
        final_total_purchase = sum(total_purchase)

        sales = Sale.todays_sales()
        total_sales = [i.product.product_price * i.quantity for i in sales]
        final_total_sales = sum(total_sales)

        return render(request, 'reports/todays_report.html', locals())