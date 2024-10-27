from django.shortcuts import render, redirect
from django.http import HttpResponse

def app_index(request):
    return render(request, 'index.html')
