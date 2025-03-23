from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from . import views
from .views import site, api


app_name = 'recipes'
recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register('', 
                              views.RecipeAPIv4List,
                            #   basename= Não é preiso informar pq a class tem um queryset
                              )


urlpatterns = [
    path('pagina_inicial/', views.RecipeListViewsHome.as_view(), name="home"),
    path('api/v1/', views.RecipeListViewsHomeApi.as_view(), name="api_v1"),
    path('api/v1/<int:pk>/', views.RecipeDetailAPI.as_view(), name="api_v1_detail"),
    path('search/', views.search, name="search"),
    path('category/<int:category_id>/', views.RecipeListViewsCategory.as_view(), name="category"),
    path('<int:id>/', views.recipe, name="recipe"),
    path('theory', views.theory, name='theory'),
    path('tags/<slug:slug>/', views.RecipeListViewTag.as_view(), name="tag"),
    path('api/v2/', api.recipe_api_list, name='all_recipe'),
    path('api/v2view/', api.RecipeAPIv2List.as_view(), name='all_recipe1'),
    path('api/v3view/', api.RecipeAPIv3List.as_view(), name='all_recipe2'),
    path('api/v2view/<int:pk>/', api.RecipeAPIv2Detail.as_view(), name='all_recipe3'),
    path('api/v3view/<int:pk>/', api.RecipeAPIv3Detail.as_view(), name='all_recipe4'),
    path('api/v2/<int:pk>/', views.recipe_api_detail, name='recipes_api_v2_detail'),
    path('api/v22/<int:pk>/', views.recipe_api_detail2, name='recipes_api_v22_detail'),
    path('api/v2/tag/<int:pk>/', views.recipe_api_tag_detail, name='recipes_api_v2_tag'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(recipe_api_v2_router.urls)),


    # path('api/v4view/', api.RecipeAPIv4List.as_view(
    #     {
    #         #Indica qual função o método vai executar 
    #         'get': 'list',
    #         'post': 'create'
    #     }
    # ), name='all_recipe5'),

    # path('api/v4view/<int:pk>/', api.RecipeAPIv4List.as_view(
    #     {
    #         #Indica que o método get vai pegar o list da class 
    #         'get': 'retrieve',
    #         'patch': 'partial_update',
    #         'delete': 'destroy',
    #     }
    # ), name='all_recipe5'),

]

#outra forma de adicionar o router
# urlpatterns += recipe_api_v2_router.urls