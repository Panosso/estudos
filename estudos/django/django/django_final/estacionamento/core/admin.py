from django.contrib import admin
from .models import (Marca,
                     Veiculo,
                     Pessoa,
                     Cor,
                     Categoria,
                     Parametros,
                     MovRotativoHora,
                     MovRotativoMes,
                     MovMensalista)

class PessoaAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'telefone', 'categoria', )

    list_display = ('id', 'nome', 'telefone', 'categoria', )

    list_filter = ('categoria', )

    search_fields = ('nome', )


class MovRotativoHoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'entrada', 'saida', 'vl_hora', 'total', 'horas_total', 'pago', 'veiculo_grid')

    def veiculo_grid(self, obj):
        #Retorna o objeto criado pela classe MovRotativoHora, portanto pode acessar todos os atributos do obj
        return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')

class MovRotativoMesAdmin(admin.ModelAdmin):
    list_display = ('id', 'entrada', 'saida', 'vl_mes', 'veiculo')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Cor)
admin.site.register(Categoria)
admin.site.register(Parametros)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativoHora, MovRotativoHoraAdmin)
admin.site.register(MovRotativoMes, MovRotativoMesAdmin)