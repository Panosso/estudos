from django.urls import resolve, reverse
from teste_recipe_base import RecipeTesteBase

from ..models import Recipe
from ..views import index_page


class RecipeViewsTest(RecipeTesteBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_views_functions_is_correct(self):
        view = resolve(reverse('recipes:recipes-home'))
        print(view)
        self.assertIs(view.func, index_page)

    def test_recipe_home_views_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_views_returns_status_404_no_recipe(self):
        response = self.client.get(reverse('recipes:category',
                                           kwargs={'category_slug': 'watabum'}))  # noqa: E501
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_views_load_correct_template(self):
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertTemplateUsed(response, 'recipes/templates/pages/home.html')

    def test_recipe_home_show_not_found_recipe(self):
        Recipe.objects.delete(pk=1)
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertIn('<h1>Não encontrei nenhuma receita</h1>',
                      response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):

        response = self.client.get(reverse('recipes:recipes-home'))
        content = response.content.decode('utf-8')
        response_context_content = response.context['recipes']

        self.assertIn('teste', content)
        self.assertIn('12 m', content)
        self.assertEqual(len(response_context_content), 1)
