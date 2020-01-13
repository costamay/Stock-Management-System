from django.shortcuts import render
from .models import *

def all_suppliers(request):
    suppliers = Supplier.objects.all()
   
    return render(request, 'suppliers.html', locals())
