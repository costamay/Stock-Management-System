from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .models import Purchase
from .forms import PurchaseForm, UpdatePurchaseForm

def purchases(request):
    purchases = Purchase.objects.all()

    return render(request, 'purchases.html',{'purchases':purchases})

def create_purchases(request):
    if request.method == 'POST' :
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.save()

        return redirect('purchases')

    else:
        form = PurchaseForm()

    return render(request, 'create_purchase.html', {'form': form})

def update_purchases(request):
    if request.method == 'POST' :
        form = UpdatePurchaseForm(request.POST,request.FILES)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.save()

        return redirect('purchases')

    else:
        form= UpdatePurchaseForm()
    return render(request,'update_purchase.html', {'form':form})

def delete_purchases(request, pk):
    template = 'purchases.html'
    Purchase.objects.filter(id=pk).delete()
    purchases = Purchase.objects.all()
    context = {
        'purchases': purchases,
    }
    return render(request, template, context)