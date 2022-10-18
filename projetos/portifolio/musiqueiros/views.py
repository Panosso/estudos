from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_musiqueiros(request):
    return HttpResponse('Olá Mundo Musiqueiros')