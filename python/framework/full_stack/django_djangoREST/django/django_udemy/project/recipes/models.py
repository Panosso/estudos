import os
import string

from random import SystemRandom
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify
from django.contrib.contenttypes.fields import GenericRelation
from tag.models import Tag
from PIL import Image
from django.db.models import F, Value
from django.db.models.functions import Concat

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class RecipeManager(models.Manager):
    def get_published(self):
        return self.filter(
            is_published=True
        ).annotate(
            author_full_name=Concat(
                F('author__first_name'), Value(' '),
                F('author__last_name'), Value(' ('),
                F('author__username'), Value(')'),
            )
        ).order_by('-id').select_related('category', 'author').prefetch_related('tags')

class Recipe(models.Model):
    objects = RecipeManager()
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
    # tags = GenericRelation(Tag, related_query_name='recipes')

    tags = models.ManyToManyField(to=Tag)


    def __str__(self):
        return self.title

    #Permite que no django admin, apareça a opção 'Ver no site'
    def get_absolute_url(self):
        return reverse('recipes:recipe', args=(self.id, ))

    @staticmethod
    def resize_image(image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)

        #LANCZOS é um algoritmo de resample
        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

    #Metodo que salva a informação, el roda toda vez que vamos salvar um registro no model
    def save(self, *args, **kwargs):

        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits,
                    k=5,
                )
            )
            self.slug = slugify(f'{self.title}-{rand_letters}')

        saved = super().save(*args, **kwargs)

        if self.cover:
            try:
                self.resize_image(self.cover, 800)
            except FileNotFoundError:
                ...

        #Chamo o métodod a class para sobreescrever
        return saved

