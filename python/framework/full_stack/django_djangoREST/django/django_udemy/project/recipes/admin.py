from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from tag.models import Tag

from .models import Category, Recipe

#Cria a class para ser adicionada no django admin
class CategoryAdmin(admin.ModelAdmin):
    ...

class TagInLine(GenericStackedInline):
    model = Tag
    fields = ('name',)

    #Quantidade de campos que vão aparecer na receita
    extra = 2

#Outro modo de adicionar um model no admin do django
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    #Na grid do admin fala quais campos devem aparecer
    list_display = ('id', 'title', 'category', 'is_published')

    #Na grid, deixa os seguintes campos como clicaveis levando assim até o registro.
    list_display_links = ('id', 'title',)

    #Onde ele vai procurar o que digitamos
    search_fields = ('title', 'description', 'slug')

    #Cria um filtro rapido do lado direito
    list_filter = ('category', 'author', 'preparation_steps_is_html')

    #Quantidade de item por pagina
    list_per_page = 10

    #Deixa o campo como editavel dentro da grid
    list_editable = ('is_published',)

    #Ordena os dados de acordo com o campo, com o sinal de negativo, é feita a ordenação decrescente
    ordering = ('-id',)

    #Quando utilizado essa vairavel, no momento que estamos preenchendo o campo da tupla, o campo slug tbm será preenchido.
    prepopulated_fields = {"slug": ["title"]}

    inlines = (TagInLine,)

#Registra o model no admin do django
admin.site.register(Category, CategoryAdmin)
