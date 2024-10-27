from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.index_page, name="recipes-home"),
    path("category/<str:category_slug>/", views.category, name="category"),
    path("search/", views.search_view, name="recipe-search"),
    path("<str:recipe_slug>/", views.recipe_view, name="recipes-recipe"),
]
