# from django.contrib import messages
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, render  # noqa: E501

from .models import Recipe
from .utils.pagination import make_pagination

# from .utils.factory import make_recipe

PER_PAGES = 9


# Create your views here.
def index_page(request):
    # Faz um filtro buscando apenas as receitas publicadas.
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    # Permite enviar mensagens como sucesso, alerta, info, warning e por ai vai
    # messages.success(request, "Deu certo os trem aqui")

    return render(
        request,
        "recipes/templates/pages/home.html",
        context={"recipes": page_obj, "pages": pagination_range},  # noqa: E501
    )


def index_page2(request):
    # Faz um filtro buscando apenas as receitas publicadas.
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/templates/pages/home.html",
        context={"recipes": recipes},  # noqa: E501
    )


def recipe_view(request, recipe_slug):
    recipe = Recipe.objects.filter(slug=recipe_slug, is_published=True).first()

    return render(
        request,
        "recipes/templates/pages/recipe-view.html",
        context={"recipe": recipe, "is_detail_page": True},
    )


def category(request, category_slug):
    #
    # Nesse método é necenssário que tenha apenas um retorno,
    # caso contrário ocorrerá um erro.
    # recipes = get_object_or_404(
    #     Recipe, category__slug=category_slug, is_published=True,)

    # Método que retorna uma lista ou um 404
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__slug=category_slug, is_published=True
        ).order_by(  # noqa: E501
            "-id"
        )
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

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

    return render(
        request,
        "recipes/templates/pages/category.html",
        context={
            "recipes": page_obj,
            "title": f"{category_name}",
            "pages": pagination_range,
        },
    )


def search_view(request):
    q = request.GET.get("q", "").strip()

    # Utilizando o 'Q' é possível fazer um filtro onde
    # será feita a pesquisa por um termo OR o outro, ao inves de ser AND
    # como é o padrão
    recipes = Recipe.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q), is_published=True
    ).order_by(
        "-id"
    )  # noqa: E501

    print(recipes.query)

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    if not q:
        raise Http404()

    return render(
        request,
        "recipes/templates/pages/search.html",
        context={
            "page_title": f'Search for "{q}" | ',
            "search_term": f'"{q}"',
            "recipes": page_obj,
            "pages": pagination_range,
            "additional_url_query": f"&q={q}",
        },  # noqa: E501
    )
