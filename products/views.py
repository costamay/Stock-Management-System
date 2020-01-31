from django.shortcuts import render,redirect,HttpResponse
from products.forms import *
from django.db.models import Q
from products.models import *
from django.contrib import messages

def product_list(request):
    query = " "
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    from sales.models import Sale
    products =  get_product_queryset(query)
    total_product = Product.objects.all().count()
    context ={
        "products":products,
        "total_product":total_product
    }
    return render(request,"products/product_list.html",locals())


def product_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id) 
            print(product)
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

def get_product_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        products = Product.objects.filter(
            Q(product_name__icontains=q) | 
            Q(product_category__icontains=q)
                ).distinct()
        for product in products:
            queryset.append(product)
    return list(set(queryset))
   
def search_products(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_products = Product.search(search_term)
        message = f"{search_term}"

        return render(request, 'products/search.html',{"message":message,"products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'products/search.html',{"message":message})

def reorder_notification(request):
    products = Product.objects.all()
    total = Product.product_qyt 
    total = 0
    for product in products:
        total = total  + int(product.product_qyt)
    if total < 2:
        messages.warning(request, 'Stock  running low ' f"{total}" ' products left')
    else:
        messages.success(request,' ' f"{total}" ' still in stock')
    return render(request, 'products/search.html',locals())
