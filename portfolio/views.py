from django.shortcuts import render
from .dados import habilidades

# Create your views here.
def home(request):
    context = {
        'habilidades': habilidades
    }
    return render(request, 'home.html', context)
