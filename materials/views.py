from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
def all_materials(request):
    materials = Material.objects.all()
    total_materials = Material.objects.all().count()
    return render(request, 'materials.html', locals())

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    else:
        form = cls()
        return render(request, 'add_new.html', locals())

def add_material(request):
    return add_item(request, MaterialForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('all_material')
    else:
        form = cls(instance=item)
        return render(request, 'edit_material.html', locals())

def edit_material(request, pk):
    return edit_item(request, pk, Material, MaterialForm)

def delete_material(request, pk):
    template = 'materials.html'
    Material.objects.filter(id=pk).delete()
    materials = Material.objects.all()
   
    return render(request, template, locals())


