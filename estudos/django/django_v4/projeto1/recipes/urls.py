from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page),
    path('<int:recipe_id>/', views.recipe_view)
]
