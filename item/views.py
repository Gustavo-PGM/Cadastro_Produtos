from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
# Create your views here.

def enviar(request):
	if request.method == 'GET':
		codi_erro = request.GET.get('codi_erro')
		text = request.GET.get('text')

		return render(request, 'enviar.html', {'codi_erro': codi_erro, 'text': text})

	elif request.method == 'POST':
		item = request.POST.get('item') #.get é para pegar
		valor = request.POST.get('valor')

		if len(item) <= 0:
			return redirect('/cadastro/enviar/?codi_erro=1&text=Digite o nome')

		item_bd = Item(
			nome = item,
			preco = valor
		)
		item_bd.save()
		return redirect('/cadastro/listar/')


def listar(request):
	nome_filtro = request.GET.get('filtrar') #O GET é o metodo
	if nome_filtro:
		produtos = Item.objects.filter(nome__icontains=nome_filtro) #filtromockup
	else:
		produtos = Item.objects.all()
	return render(request, 'listar.html', {'produtos': produtos})


def delet(request, id):	
	prodelet = Item.objects.get(id=id)
	prodelet.delete()
	return redirect('/cadastro/listar/')
