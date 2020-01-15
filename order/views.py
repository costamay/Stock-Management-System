from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm, UpdateOrderForm


def orders(request):
    orders = Order.objects.all()
    

    return render(request, 'Order/orders.html',{'orders':orders})


def create_orders(request):
    if request.method == 'POST' :
        form = OrderForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            # order.delivery=1
            order.save()

        return redirect('orders')

    else:
        form = OrderForm()

    return render(request, 'Order/add_order.html', {'form': form})

def update_orders(request):
    if request.method == 'POST' :
        form = UpdateOrderForm(request.POST,request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

        return redirect('orders')

    else:
        form= UpdateOrderForm()
    return render(request,'update_order.html', {'form':form})

def delete_orders(request, pk):
    template = 'order.html'
    Order.objects.filter(id=pk).delete()
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, template, context)

def search_orders(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        orders = Order.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'search_orders.html', {'orders': orders, 'message': message})
        
    return render(request, 'search_orders.html')

    