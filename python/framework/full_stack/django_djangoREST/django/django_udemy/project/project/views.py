import os

from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

from recipes.models import Recipe

def home_page(request):
    return render(request, 'global/home_site.html', context={
        'app_name': 'Home Page Site',
        'icon_app': 'fas fa-home main-logo-icon'
    })