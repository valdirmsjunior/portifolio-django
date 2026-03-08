from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('sobre/', views.sobre_min, name='sobre'),
]