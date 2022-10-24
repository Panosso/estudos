from django.urls import path

from recipes.views import aqui, base_html, index, temp_html

urlpatterns = [
    path('', index),
    path('aqui/', aqui),
    path('base/', base_html),
    path('temp/', temp_html)
]
