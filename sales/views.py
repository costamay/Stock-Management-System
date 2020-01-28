from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from sales.forms import *
from products.models import *
from sales.models import Sale


def sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales/all_sales.html', locals())


def sales_report(request):
    sales = Sale.objects.all()
    total = [i.product.product_price * i.quantity for i in sales]
    final_total = sum(total)
    return render(request, 'reports/sales_report.html', locals())

def add_item(request,cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            obj = Product.objects.filter(id=request.POST['product']).first()
            obj.product_qyt = obj.product_qyt - int(request.POST['quantity'])
            obj.save()
            form.save()
            return redirect('sales')
    else:
        form = cls()
        return render(request, 'sales/add_sell.html', locals())


def add_sell(request):
    return add_item(request, SalesForm)

def sell_product(request,id):
    item = get_object_or_404(Product,id=id)
    print(item)


def filter(request):
    sales = Sale.objects.filter(date__range=(
        request.POST['start_date'],
        request.POST['end_date']
    ))
    
    total = [i.product.product_price * i.quantity for i in sales]
    final_total = sum(total)
    
    return render(request, 'reports/sales_report.html',locals())