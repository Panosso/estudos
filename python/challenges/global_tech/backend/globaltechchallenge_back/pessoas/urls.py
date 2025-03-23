from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'person'
person_api_router = SimpleRouter()
person_api_router.register('api/lista_pessoas', 
                              views.PersonAPIList,
                              )

urlpatterns = [
    path('', include(person_api_router.urls))
    ]