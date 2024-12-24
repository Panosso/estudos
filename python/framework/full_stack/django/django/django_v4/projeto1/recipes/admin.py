from django.contrib import admin

from .models import Category, Recipe

# Register your models here.

# é possível registar  site cmo esse decorator
# @admin.register


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
