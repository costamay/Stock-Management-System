from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .models import Order

def orders(request):
    orders = Order.objects.all()

    return render(request, 'orders.html',{'orders':orders})

