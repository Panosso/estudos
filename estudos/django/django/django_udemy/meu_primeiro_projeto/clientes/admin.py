from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

# Register your models here.

#Personalizar a classe admin.
class EmpregadoAdmin(admin.ModelAdmin):
    #Campos que serão preenchidos em uma adição
    fields = ('nome', 'endereco')

    #Campos que iram aparecer no grid
    list_display = ('id', 'nome', 'endereco', 'email')

    #Bloco de filtro que terá no django admin
    list_filter = ('departamento', )

    #Barra de pesquisa que irá filtrar os cmapos mencionados aqui
    search_fields = ('id', 'nome')

#Para a classe criada em models.py aparecer no Django admin é necessário importar aqui no admin.py
# e então adicionar a linha admin.site.register(<nome_classe>)
admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)