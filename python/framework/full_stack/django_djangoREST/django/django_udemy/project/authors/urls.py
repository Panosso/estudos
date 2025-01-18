from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'authors'

author_api_router = SimpleRouter()
author_api_router.register('api', views.AuthorViewSet, basename='author-api')

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard/recipe/<int:id>/edit/', views.dashboard_recipe_edit, name='dashboard_recipe_edit'),

    #Passando uma class view como view, usando o método as_view
    path('dashboard/recipe/<int:id_receita>/edit/', views.DashboardRecibe.as_view(), name='dashboard_recipe_edit'),
    path('dashboard/recipe/new', views.DashboardRecibe.as_view(), name='dashboard_recipe_new'),
    path('dashboard/recipe/delete/', views.DashboardRecibeDelete.as_view(), name='dashboard_recipe_delete'),

]

urlpatterns += author_api_router.urls