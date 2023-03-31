from django.db import models

# Create your models here.


class Recipe(models.Model):
    # varchar
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # Auto now add --> Coloca a data uma unica vez no momento da criação
    created_at = models.DateTimeField(auto_now_add=True)
    # Auto now --> Atualiza a data de criação no momento do update
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # Define qual pasta vai colocar a imagem
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/')
