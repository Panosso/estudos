"""meu_primeiro_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from clientes.views import home, clientes, cliente_detalhe, cliente_nome, produtos
#Gambiarra do Django para pode ver a imagem mesmo em teste.
# visto que em produção existem outros meios para poder ver a imagem.
from django.conf import settings
from django.conf.urls.static import static

#Nessa lista é adicionado as querys que o site vai ter.
urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^clientes/$', clientes),
    url(r'^cliente/(?P<id_cliente>\d+)$', cliente_detalhe),
    url(r'^cliente/(?P<nome_cliente>\w+)$', cliente_nome),
    url(r'^cliente/(?P<nome_cliente>\w+)$', cliente_nome),
    url(r'^produtos/$', produtos)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Parte da gambiarra.
