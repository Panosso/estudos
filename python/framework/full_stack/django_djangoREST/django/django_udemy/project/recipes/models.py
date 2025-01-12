from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify
from django.contrib.contenttypes.fields import GenericRelation
from tag.models import Tag


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    #Gera a relação com o model de tags
    tags = GenericRelation(Tag, related_query_name='recipes')


    def __str__(self):
        return self.title

    #Permite que no django admin, apareça a opção 'Ver no site'
    def get_absolute_url(self):
        return reverse('recipes:recipe', args=(self.id, ))

    #Metodo que salva a informação, el roda toda vez que vamos salvar um registro no model
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        #Chamo o métodod a class para sobreescrever
        return super().save(*args, **kwargs)

