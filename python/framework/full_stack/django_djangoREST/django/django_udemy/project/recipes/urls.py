from django.urls import path

from . import views
from .views import site, api

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
    path('api/v2/', api.recipe_api_list, name='all_recipe'),
    path('api/v2/<int:pk>/', views.recipe_api_detail, name='recipes_api_v2_detail'),
    path('api/v22/<int:pk>/', views.recipe_api_detail2, name='recipes_api_v22_detail'),
    path('api/v2/tag/<int:pk>/', views.recipe_api_tag_detail, name='recipes_api_v2_tag'),
]

