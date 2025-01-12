from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewsHome.as_view(), name="home"),
    path('api/v1/', views.RecipeListViewsHomeApi.as_view(), name="api_v1"),
    path('api/v1/<int:pk>/', views.RecipeDetailAPI.as_view(), name="api_v1_detail"),
    path('search/', views.search, name="search"),
    path('category/<int:category_id>/', views.RecipeListViewsCategory.as_view(), name="category"),
    path('<int:id>/', views.recipe, name="recipe"),
    path('theory', views.theory, name='theory'),
    path('tags/<slug:slug>/', views.RecipeListViewTag.as_view(), name="tag"),
]

