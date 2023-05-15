from django.test import TestCase
from django.urls import reverse

from ..models import Category


# Create your tests here.
class RecipeURLsTest(TestCase):
    # Cria uma função que vai testar se os testes
    # que foram configurados no pytest estão OK
    # para executa-los é necessário ir no terminal e digitar pytest
    def test_the_pytest_is_ok(self):
        print("Ola Mundo")
        assert 1 == 1, "Um é igual a um"

    def test_recipe_home_url_is_correct(self):
        home_url = reverse("recipes:recipes-home")
        self.assertEqual(home_url, "/recipes/")

        all_category = list(Category.objects.all())

        for cat in all_category:
            recipe_category = reverse(
                "recipes:category", kwargs={"category_slug": cat}
            )  # noqa: E501
            self.assertEqual(recipe_category, f"/recipes/category/{cat}")

    def test_recipe_search_url(self):
        url = reverse("recipes:recipe-search")
        self.assertEqual(url, "/recipe/search/")
