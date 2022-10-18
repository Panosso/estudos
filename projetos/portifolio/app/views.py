from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_apps(request):
    return HttpResponse('Olá Mundo Index App')