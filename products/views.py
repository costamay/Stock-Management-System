from django.shortcuts import render
from products.forms import *


def product(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('all_product')
            except:
                pass
        else:
            form = ProductForm()
    return render(request,'Products/product.html',{'form':form})

def all_product(request):  
    product = Product.objects.all()  
    return render(request,"Product/product.html",{'product':product})  

def edit_product(request):
    product = Product.objects.get(id=id)
    return render(request,'Products/product-edit.html',{'product':product})

def update_product(request):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST,instance = product)
    if form.is_valid():
        form.save()
        return redirect('/product-page')
    return render(request,'Products/product-edit.html',{'product':product})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return render("/product-page")