from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Supplier

def suppliers(request):
    suppliers = Supplier.objects.all()
    
    return render(request, 'suppliers.html',{"suppliers": suppliers})