from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *

def all_suppliers(request):
    suppliers = Supplier.objects.all()
   
    return render(request, 'suppliers.html', locals())

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_suppliers')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

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
        return render(request, 'edit_item.html', {'form': form})

def edit_supplier(request, pk):
    return edit_item(request, pk, Supplier, SupplierForm)

def delete_supplier(request, pk):
    template = 'suplliers.html'
    Supplier.objects.filter(id=pk).delete()
    suppliers = Supplier.objects.all()
    context = {
        'items': items,
    }
    return render(request, template, context)
