from django.shortcuts import render
from .dados import habilidades, projetos, sobre

# Create your views here.
def home(request):
    context = {
        'habilidades': habilidades
    }
    return render(request, 'home.html', context)

def lista_projetos(request):
    context = {
        'projetos': projetos
    }
    return render(request, 'projetos.html', context)

def sobre_min(request):
    context = {
        'info': sobre
    }
    return render(request, 'sobre.html', context)
    