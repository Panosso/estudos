from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('category/<int:category_id>/',
         views.category, name="category"),
    path('<int:id>/', views.recipe, name="recipe"),
]
