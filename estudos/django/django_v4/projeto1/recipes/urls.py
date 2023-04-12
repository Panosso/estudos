from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index_page, name='recipes-home'),
    path('category/<str:category_name>/', views.recipe, name='category'),
    path('<int:recipe_id>/', views.recipe_view, name='recipes-recipe')
]
