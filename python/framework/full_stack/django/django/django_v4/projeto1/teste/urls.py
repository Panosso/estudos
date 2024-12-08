from django.urls import path

from teste.views import teste1

app_name = 'teste'

urlpatterns = [
    path('teste1/', teste1)
]
