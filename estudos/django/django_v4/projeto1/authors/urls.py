from django.urls import path

from .views import register_create, register_view

app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("register/create/", register_create, name="create"),
]
