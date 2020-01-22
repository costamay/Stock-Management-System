from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth import login,authenticate
from login.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from login.forms import UserForm

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
        raise Http404()
    context = {}
    template = "dashboards/home.html"
    return render(request,template,context)

    


def shome(request):
    template = "dashboards/dashboard_stock.html"
    return render(request,template)

def achome(request):
    template = "dashboards/dashboard_accountant.html"
    return render(request,template)

def ahome(request):
    template = "dashboards/dashboard_admin.html"
    return render(request,template)


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
            user = User.objects.get(pk,id) 
            print(user,"fffffffffffff")
            form = UserForm(instance=product)
        return render(request,"accounts/accounts_form.html",{'form':form})
    else:
        if id == 0:
            form = UserForm(request.POST,request.FILES)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST,instance=user) 
        if form.is_valid():
            form.save()
        return redirect('/users')

def delete_user(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/users/list')