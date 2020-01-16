from django.shortcuts import render,redirect
from products.forms import *


def product_list(request):
    products =  Product.objects.all()
    context ={
        "products":products
    }
    return render(request,"products/product_list.html",context)

        
def product_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id) 
            form = ProductForm(instance=product)
        return render(request,"products/product_form.html",{'form':form})
    else:
        if id == 0:
            form = ProductForm(request.POST,request.FILES)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance=product) 
        if form.is_valid():
            form.save()
        return redirect('/products/list')

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/products/list')
