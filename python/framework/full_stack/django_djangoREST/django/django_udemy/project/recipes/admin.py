from django.contrib import admin

from .models import Category, Recipe

#Cria a class para ser adicionada no django admin
class CategoryAdmin(admin.ModelAdmin):
    ...


#Outro modo de adicionar um model no admin do django
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


#Registra o model no admin do django
admin.site.register(Category, CategoryAdmin)
