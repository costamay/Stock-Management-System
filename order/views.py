from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm


def orders(request):
    orders = Order.objects.all()

    return render(request, 'orders.html',{'orders':orders})


def create_orders(request):
    if request.method == 'POST' :
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

        return redirect('orders')

    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})