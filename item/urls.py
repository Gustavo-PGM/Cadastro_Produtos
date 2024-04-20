from django.urls import path, include
from . import views

urlpatterns = [
     path('enviar/', views.enviar, name='enviar'),
     path('listar/', views.listar, name='listar'),
     path('delet/<int:id>/', views.delet, name='delet'), #int = valor da variavel quer receber
]