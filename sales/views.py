from django.shortcuts import render
from .models import *

def sales_report(request):
    sales = Sale.objects.all()
    return render(request, 'reports/sales_report.html', locals())


