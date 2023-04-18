from django.shortcuts import get_list_or_404, render

from .models import Recipe
from .utils.factory import make_recipe


# Create your views here.
def index_page(request):
    # Faz um filtro buscando apenas as receitas publicadas.
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
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


def category(request, category_slug):

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__slug=category_slug,
            is_published=True).order_by('-id'))

    category_name = recipes[0].category.name

    # # Retorno do 404 3 métodos;
    # # Imports necessários
    # from django.http.response import Http404, HttpResponse
    # if not recipes:
    #     # Metodo 1
    #     # return HttpResponse(content='Not Found', status=404)

    #     # Metodo 2
    #     raise Http404('Not Found 2')

    # # O método getattr verifica se a variavel possui o atributo, caso possuir
    # #   retorna ele, caso não retorna o terceira termo

    # # No getattr interno verifica se recipes possui um atributo chamado
    # #   'category' caso possua será retornado o atributo
    # #   category(que é o obj category), caso não possua será retornado None

    # # No getattr externo, é verificado se o getattr interno retornou a
    # #   categoria, caso sim será retornado o nome da categoria,
    # #   caso não será retornado o texto 'Not Found'

    # category_name = getattr(
    #     getattr(recipes.first(), 'category', None),
    #     'name',
    #     'Not found'
    # )

    return render(request, 'recipes/templates/pages/category.html',
                  context={
                      'recipes': recipes,
                      'title': f'{category_name}'
                  })
