from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    minha_var = 'Jaque'
    sexo = 'f'
    lista_nome = [
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Jaque', 'sexo': 'f'},
        {'nome': 'Yago', 'sexo': 'm'}
        ]
    dados = {'nome': minha_var, 'sexo': sexo, 'lista_index': lista_nome}
    return render(request, 'index.html', dados)

def produtos(request):
    return render(request, 'produtos.html')

def clientes(request):
    return HttpResponse([x for x in ['Tico', 'Teko']])

def cliente_detalhe(request, id_cliente):
    return HttpResponse(f'Detalhe do arrombado {id_cliente}')

def cliente_nome(request, nome_cliente):
    return HttpResponse(f'Nome do arrombado {nome_cliente}')
