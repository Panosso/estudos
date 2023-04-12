from django.shortcuts import render

from .models import Recipe
from .utils.factory import make_recipe


# Create your views here.
def index_page(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/templates/pages/home.html',
                  context={
                      'recipes': recipes
                  })


def recipe_view(request, recipe_id):
    return render(request, 'recipes/templates/pages/recipe-view.html',
                  context={
                      'recipe': make_recipe,
                      'is_detail_page': True
                  })


def recipe(request, category_name):
    recipes = Recipe.objects.filter(
        category__name=category_name).order_by('-id')
    return render(request, 'recipes/templates/pages/home.html',
                  context={
                      'recipes': recipes
                  })
