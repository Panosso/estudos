from django.test import TestCase

from ..models import Category, Recipe, User


class RecipeTesteBase(TestCase):
    def setUp(self) -> None:
        cat = self.make_cat()
        # Faz algumas validações antes de salvar no banco
        cat.full_clean()
        # Salva a categoria no banco criado pelos tests
        cat.save()

        author = self.make_author()

        author.full_clean()
        author.save()

        recipe = self.make_recipe(author=author, cat=cat)

        recipe.full_clean()
        recipe.save()

        return super().setUp()

    def make_cat(self):
        return Category.objects.create(name="Teste", slug="teste")

    def make_author(self):
        return User.objects.create_user(
            first_name="user",
            last_name="name",
            username="username",
            password="123456",
            email="username@gmail.com",
        )

    def make_recipe(self, author=None, cat=None):
        return Recipe.objects.create(
            category=cat,
            author=author,
            title="teste",
            description="testetestetestetestetesteteste",
            slug="teste",
            preparation_time="12",
            preparation_time_unit="m",
            servings="2",
            preparation_steps="testetestetestetestetestetesteteste",
            preparation_steps_is_html=False,
            is_published=True,
            cover="D:\Projetos\projects_estudos\estudos\django\django_v4\projeto1\\recipes\cover\\2023\\04\\06\Screenshot_2022-11-16_at_09-06-01_Seal_Any_Bag_Tightly_-_Funny.png",  # noqa: E501
        )

    def get_recipe(self):
        return Recipe.objects.get(pk=1)
