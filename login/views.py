from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from login.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from login.forms import UserForm
from materials.models import *
from sales.models import *
from supplier.models import *
from client.models import *

from purchase.models import *
from products.models import *


# test for categoriesgitch

# def supplier(request):

#     return render(request, 'supplier/manage_supplier.html',locals())


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
        return redirect(home)
    context = {}
    template = "dashboards/home.html"
    return render(request,template,context)

    

@user_passes_test(lambda u:u.is_active and u.groups.filter(name='store_manager'),redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login')
def shome(request):
    products = Product.objects.all()[:5]
    total_materials_stock = Material.objects.all().count()
    total_sales_stock = Sale.objects.all().count()
    total_supplier_stock = Supplier.objects.all().count
    total_client_stock = Client.objects.all().count()
    total_purchase_stock = Purchase.objects.all().count()
    total_product_stock = Product.objects.all().count() 
    template = "dashboards/dashboard_stock.html"
    return render(request,template, locals())


@user_passes_test(lambda u:u.is_active and u.groups.filter(name='accountant'),redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login')
def achome(request):
    products = Product.objects.all()[:5]
    total_materials_acc = Material.objects.all().count()
    total_sales_acc = Sale.objects.all().count()
    total_client_acc = Client.objects.all().count()
    total_purchase_acc = Purchase.objects.all().count()
    total_product_acc = Product.objects.all().count() 
    total_supplier_acc = Supplier.objects.all().count
    template = "dashboards/dashboard_accountant.html"
    return render(request,template, locals())


def main(request):
    products = Product.objects.all()[:5]
    total_materials_acc = Material.objects.all().count()
    total_sales_acc = Sale.objects.all().count()
    total_client_acc = Client.objects.all().count()
    total_purchase_acc = Purchase.objects.all().count()
    total_product_acc = Product.objects.all().count() 
    total_supplier_acc = Supplier.objects.all().count
    template = "dashboards/main.html"
    return render(request,template, locals())

@user_passes_test(lambda u:u.is_active and u.groups.filter(name='admin'),redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login')
def ahome(request):
    products = Product.objects.all()[:5]
    total_materials_admin = Material.objects.all().count()
    total_sales_admin = Sale.objects.all().count()
    total_supplier_admin = Supplier.objects.all().count
    total_client_admin = Client.objects.all().count()
    total_purchase_admin = Purchase.objects.all().count()
    total_product_admin = Product.objects.all().count()    

    template = "dashboards/dashboard_admin.html"
    return render(request,template,locals())


def users_list(request):
    users =  User.objects.all()
    context ={
        "users":users,
    }
    return render(request,"accounts/accounts_list.html",locals())



def users_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id) 
           
            form = UserForm(instance=user)
        return render(request,"accounts/accounts_form.html",{'form':form})
    else:
        if id == 0:
            form = UserForm(request.POST,request.FILES)
            
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST,instance=user) 
        if form.is_valid():
            form = form.save(commit=False)
            password = request.POST['password']
            form.set_password(request.POST['password'])
            form.save()
        return redirect('/users')

def delete_user(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/users/list')



