from .teste_recipe_base import RecipeTesteBase


class RecipeModelTest(RecipeTesteBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_title_long(self):
        # recipe = self.recipe
        self.recipe.title = "a" * 100
        self.recipe.full_clean()
        self.recipe.save()
        self.fail(len(self.recipe.title))
        ...
