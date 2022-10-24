from django.urls import path

from teste.views import teste1

urlpatterns = [
    path('teste1/', teste1)
]
