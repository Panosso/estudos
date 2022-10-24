from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Index Page')


def base_html(request):
    nome_programador = 'Pedro'
    context = {'name': nome_programador}
    return render(request, 'base_template.html', context=context)


def temp_html(request):
    nome_programador = 'Pedro'
    context = {'name': nome_programador}
    return render(request, 'temp.html', context=context)


def aqui(request):
    nome_programador = 'Pedro'
    context = {'name': nome_programador}
    return render(request, 'home.html', context=context)
