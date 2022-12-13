from django.shortcuts import render


# Create your views here.
def index_page(request):
    return render(request, 'recipes/templates/pages/home.html',
                  {'name': 'Pedro Machado'})


def recipe_view(request, recipe_id):
    return render(request, 'recipes/templates/pages/recipe-view.html',
                  {'name': recipe_id})
