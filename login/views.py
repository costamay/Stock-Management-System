from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth import login,authenticate
from login.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import Http404
from products.models import *
from purchase.models import *
from client.models import *
from supplier.models import *
from sales.models import *
from materials.models import *
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get("passowrd")
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            typ_obj = user_type.objects.get(user=user)

            if user.is_authenticated and typ_obj.is_accountant:
                return redirect('achome')
            elif user.is_authenticated and typ_obj.is_manager:
                return redirect('shome')
            elif user.is_authenticated and typ_obj.is_staff:
                return redirect('ahome')
        else:
            return redirect('home')
            
@login_required(login_url='/accounts/login')
def home(request):
    grp = request.user.groups.filter(user=request.user)[0]
    print(request.user.groups)
    print(request.user)
    if grp.name == "store_manager":
        return redirect(reverse(shome))
    elif grp.name == "accountant":
        return redirect(reverse(achome))
    elif grp.name == "admin":
        return redirect(reverse(ahome))
    else:
        raise Http404()
    context = {}
    template = "dashboards/home.html"
    return render(request,template,context)

    


def shome(request):
    total_materials_stock = Material.objects.all().count()
    total_sales_stock = Sale.objects.all().count()
    total_supplier_stock = Supplier.objects.all().count
    total_client_stock = Client.objects.all().count()
    total_purchase_stock = Purchase.objects.all().count()
    total_product_stock = Product.objects.all().count() 
    template = "dashboards/dashboard_stock.html"
    return render(request,template, locals())

def achome(request):
    total_materials_acc = Material.objects.all().count()
    total_sales_acc = Sale.objects.all().count()
    total_client_acc = Client.objects.all().count()
    total_purchase_acc = Purchase.objects.all().count()
    total_product_acc = Product.objects.all().count() 
    total_supplier_acc = Supplier.objects.all().count
    template = "dashboards/dashboard_accountant.html"
    return render(request,template, locals())

def ahome(request):
    total_materials_admin = Material.objects.all().count()
    total_sales_admin = Sale.objects.all().count()
    total_supplier_admin = Supplier.objects.all().count
    total_client_admin = Client.objects.all().count()
    total_purchase_admin = Purchase.objects.all().count()
    total_product_admin = Product.objects.all().count()    

    template = "dashboards/dashboard_admin.html"
    return render(request,template,locals())


