from django.shortcuts import render, redirect
from .models import *

def all_materials(request):
    materials = Material.objects.all()
    context = {
        'materials':materials
    }
    return render(request, 'materials.html', context)

