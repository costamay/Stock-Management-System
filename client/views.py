from django.shortcuts import render,redirect
from client.models import Client
from client.forms import ClientForm

def client_list(request):
    clients =  Client.objects.all()
    context ={
        "clients":clients
    }
    return render(request,"clients/client_list.html",context)

        
def client_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ClientForm()
        else:
            client = Client.objects.get(pk=id) 
            form = ClientForm(instance=product)
        return render(request,"clients/client_form.html",{'form':form})
    else:
        if id == 0:
            form = ClientForm(request.POST,request.FILES)
        else:
            client = Product.objects.get(pk=id)
            form = ClientForm(request.POST,instance=client) 
        if form.is_valid():
            form.save()
        return redirect('/clients/list')

def delete_client(request,id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('/clients/list')
