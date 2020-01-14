from django.shortcuts import render

# Create your views here.
def client(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/product-page')
            except:
                pass
        else:
            form = ProductForm()
    return render(request,'index.html',{'form':form})


def edit_client(request):
    product = Product.objects.get(id=id)
    return render(request,'product-edit.html',{'product':product})

def update_client(request):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST,instance = product)
    if form.is_valid():
        form.save()
        return redirect('/product-page')
    return render(request,'product-edit.html',{'product':product})

def delete_client(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return render("/product-page")