from django.urls import path

from .views import login_create, login_view, register_create, register_view

app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("register/create/", register_create, name="create"),
    path("login/", login_view, name="login"),
    path("login/create/", login_create, name="login_create"),
]
