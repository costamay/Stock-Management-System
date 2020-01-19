from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm, UpdateOrderForm


def orders(request):
    orders = Order.objects.all()
    

    return render(request, 'Order/manage_orders.html',{'orders':orders})


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

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = cls(instance=item)

        return render(request, 'Order/manage_order.html', {'form': form})

def update_orders(request, pk):
    return edit_item(request, pk, Order, UpdateOrderForm)


def delete_orders(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order/orders')

    