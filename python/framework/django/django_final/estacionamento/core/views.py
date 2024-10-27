from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (Pessoa,
                     Veiculo,
                     MovRotativoHora,
                     MovRotativoMes,
                     Categoria,
                     Cor,
                     Marca,
                     Parametros)

from .forms import (PessoaForm,
                    VeiculoForm,
                    MovRotHoraForm,
                    MovRotMesForm,
                    CategoriaForm,
                    CorForm,
                    MarcaForm,
                    ParametrosForm
                    )

# Create your views here.
def home(request):

    contexto2 = {'mensagem': 'Ola Mundo12',
                'titulo': 'Django index12'}

    contexto = {'mensagem': 'Ola Mundo',
                'titulo': 'Django index',
                'contexto': contexto2}

    return render(request, 'core/html/index.html', contexto)

#Pessoa
def cadastro_pessoas(request):
    form = PessoaForm()

    contexto = {'titulo_pagina': 'Lista de cadastros', 'pessoas': Pessoa.objects.all(), 'form': form}

    return render(request, 'core/html/lista_pessoas.html', contexto)

#Recebemos o valor do form e então salvamos caso ele seja valido.
def cadastro_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoas')

def update_pessoa(request, id_cadastro):
    data = {}

    #Vai pegar o id da pessoa que vai atualizada
    pessoa = Pessoa.objects.get(id=id_cadastro)

    #Instancia o form, porém com a instancia de pessoa, para carregar no form
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    #Verifica se o form informado é valido para ser salvo,
    # caso nao seja, é renderizada a página para atualiza-lo
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pessoas')
    else:
        return render(request, 'core/html/update_pessoa.html', data)


# Veiculo
def cadastro_veiculos(request):
    #Pegamos a estrutura que criamos em form.py e passamos para o html
    form = VeiculoForm()
    contexto = {'titulo_pagina': 'Lista de veiculos', 'veiculos': Veiculo.objects.all(), 'form': form}
    return render(request, 'core/html/lista_veiculos.html', contexto)

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('veiculos')

def update_veiculo(request, id_veiculo):
    data = {}

    veiculo = Veiculo.objects.get(id=id_veiculo)

    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('veiculos')
    else:
        return render(request, 'core/html/update_veiculo.html', data)

def delete_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id=id_veiculo)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculos')

    else:
        return render(request, 'core/html/del_confirm.html', {'veiculo': veiculo})

#Rotatividade por Hora
def rot_hora(request):
    form = MovRotHoraForm()
    contexto = {'titulo_pagina': 'Rotação de veiculos por hora',
                'rot_hora': MovRotativoHora.objects.all(),
                'form': form}
    return render(request, 'core/html/mov_rot_hora.html', contexto)

def mov_rot_hora(request):
    form = MovRotHoraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('rotativos_hora')


#Rotatividade por Mes
def rot_mes(request):
    form = MovRotMesForm()
    contexto = {'titulo_pagina': 'Rotação de veiculos por mes',
                'rot_mes': MovRotativoMes.objects.all(),
                'form': form}

    return render(request, 'core/html/mov_rot_mes.html', contexto)

def mov_rot_mes(request):
    form = MovRotMesForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('rotativos_mes')


#Parametros Gerais
def parametros_gerais(request):

    form = {'cor' : CorForm(), 'categoria' : CategoriaForm(), 'marca' : MarcaForm(), 'parametros' : ParametrosForm()}

    parametros = {
        'cor': Cor.objects.all(),
        'categoria': Categoria.objects.all(),
        'marca': Marca.objects.all(),
        'parametros_gerais': Parametros.objects.all()
    }
    contexto = {'titulo_pagina': 'Parametros',
                'form': form,
                'parametros': parametros}

    return render(request, 'core/html/parametros.html', contexto)

def cor_nova(request):
    form = CorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('parametros_gerais')

def update_cor(request, id_cor):

    cor = Cor.objects.get(id=id_cor)

    form = CorForm(request.POST or None, instance=cor)

    data = {'cor': cor,
            'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('parametros_gerais')
    else:
        return render(request, 'core/html/update_cor.html', data)


def categoria_nova(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('parametros_gerais')

def update_categoria(request, id_categoria):

    categoria = Categoria.objects.get(id=id_categoria)

    form = CategoriaForm(request.POST or None, instance=categoria)

    data = {'categoria': categoria,
            'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('parametros_gerais')
    else:
        return render(request, 'core/html/update_categoria.html', data)

def marca_nova(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('parametros_gerais')

def update_marca(request, id_marca):

    marca = Marca.objects.get(id=id_marca)

    form = MarcaForm(request.POST or None, instance=marca)

    data = {'marca': marca,
            'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('parametros_gerais')
    else:
        return render(request, 'core/html/update_marca.html', data)











