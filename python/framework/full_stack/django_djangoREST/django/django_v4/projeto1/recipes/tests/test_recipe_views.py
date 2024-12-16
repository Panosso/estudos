from unittest import skip

from django.urls import resolve, reverse

from ..views import index_page
from .teste_recipe_base import RecipeTesteBase


class RecipeViewsTest(RecipeTesteBase):
    def test_recipe_home_views_functions_is_correct(self):
        view = resolve(reverse("recipes:recipes-home"))
        print(view)
        self.assertIs(view.func, index_page)

    def test_recipe_home_views_returns_status_code_200_OK(self):
        response = self.client.get(reverse("recipes:recipes-home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_views_returns_status_404_no_recipe(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_slug": "watabum"})
        )  # noqa: E501
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_views_load_correct_template(self):
        response = self.client.get(reverse("recipes:recipes-home"))
        self.assertTemplateUsed(response, "recipes/templates/pages/home.html")

    # Decorator usado para 'escapar' do teste, quando é necessário para um trabalho # noqa: E501
    @skip("WIP")
    def test_recipe_home_show_not_found_recipe(self):
        response = self.client.get(reverse("recipes:recipes-home"))
        self.assertIn(
            "<h1>Não encontrei nenhuma receita</h1>",
            response.content.decode("utf-8"),  # noqa: E501
        )

        # Força o testa a falhar, lembrando assim que tem mais coisa pra testar
        # self.fail("Tenho que escrever mais coisas sobre o test")

    def test_recipe_home_template_loads_recipes(self):
        response = self.client.get(reverse("recipes:recipes-home"))
        content = response.content.decode("utf-8")
        response_context_content = response.context["recipes"]

        self.assertIn("teste", content)
        self.assertIn("12 m", content)
        self.assertEqual(len(response_context_content), 1)

    def test_recipe_category_template_loads_recipes(self):
        # Retorno o template/html gerado pelo django
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_slug": "teste"})
        )  # noqa: E501
        print(response)
        # <HttpResponse status_code=200, "text/html; charset=utf-8">
        content = response.content.decode("utf-8")

        self.assertIn(self.make_recipe().title, content)

    def test_recipe_template_dont_load_recipes_not_published(self):
        recipe = self.get_recipe()
        recipe.is_published = False
        recipe.save()

        response = self.client.get(reverse("recipes:recipes-home"))
        self.assertIn(
            "<h1>Não encontrei nenhuma receita</h1>",
            response.content.decode("utf-8"),  # noqa: E501
        )

    def tearDown(self) -> None:
        return super().tearDown()
