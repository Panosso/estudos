from django.shortcuts import render

from .utils.factory import make_recipe


# Create your views here.
def index_page(request):
    return render(request, 'recipes/templates/pages/home.html',
                  context={
                      'recipes': [make_recipe for _ in range(10)]
                  })


def recipe_view(request, recipe_id):
    return render(request, 'recipes/templates/pages/recipe-view.html',
                  context={
                      'recipe': make_recipe,
                      'is_detail_page': True
                  })
