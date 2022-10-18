from django.urls import path
from .views import index_musiqueiros

urlpatterns = [
    path('', index_musiqueiros, name='index')
]