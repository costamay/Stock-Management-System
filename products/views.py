from django.shortcuts import render,redirect,HttpResponse
from products.forms import *
from django.db.models import Q

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



def search_product(request):
    if 'search' in request.GET and request.GET['search']:
        category = request.GET.get('search')
        results = Product.search(category)
        message = f"category"
        context = {
            results: results,
            message: message
        }
        return render(request,'results.html',locals())
    else:
        message = "You have not madce any search"
    return render(request,'results.html',{"message": message})


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
    
