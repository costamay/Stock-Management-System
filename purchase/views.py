from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from .models import Purchase
from .forms import PurchaseForm, UpdatePurchaseForm

def purchases(request):
    purchases = Purchase.objects.all()

    return render(request, 'purchase/manage_purchase.html',{'purchases':purchases})

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

    return render(request, 'purchase/add_purchase.html', {'form': form})



def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('purchases')
    else:
        form = cls(instance=item)

        return render(request, 'purchase/manage_purchase.html', {'form': form})

def update_purchases(request, pk):
    return edit_item(request, pk, Purchase, UpdatePurchaseForm)


def delete_purchases(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase.delete()
    return redirect('purchases')

