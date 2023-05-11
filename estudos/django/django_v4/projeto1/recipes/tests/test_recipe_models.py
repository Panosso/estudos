from django.core.exceptions import ValidationError
from parameterized import parameterized, parameterized_class

from ..models import Recipe
from .teste_recipe_base import RecipeTesteBase


class RecipeModelTest(RecipeTesteBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_title_long(self):
        self.recipe.title = "a" * 100

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
        ]
    )
    def test_recipe_fields_max_lenght(self, field, max_len):
        setattr(self.recipe, field, "A" * (max_len + 100))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    # def test_recipe_fields_max_lenght(self):
    #     fields = [
    #         ("title", 65),
    #         ("description", 165),
    #         ("preparation_time_unit", 65),
    #     ]  # noqa: E501

    #     for field, max_len in fields:
    #         # Subtest não da um erro logo de cara, ]
    #         # ele executa o teste de todos os itens do for
    #         with self.subTest(field=field, max_len=max_len):
    #             # Setattr, isso é equivalente a
    #             # self.recipe.field = 'A' * (max_len + 1)
    #             # porém para funcionar dentro do for,
    #             # é necessário fazer essa atribuição dinamica
    #             # e para fazer isso é necessário usar o setattr
    #             setattr(self.recipe, field, "A" * (max_len + 100))
    #             with self.assertRaises(ValidationError):
    #                 self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = Recipe(
            category=self.make_cat("maromba", "maromba"),
            author=self.make_author("outrouser"),
            title="teste",
            description="testetestetestetestetesteteste",
            slug="teste",
            preparation_time="12",
            preparation_time_unit="m",
            servings="2",
            preparation_steps="testetestetestetestetestetesteteste",
        )

        recipe.full_clean()
        recipe.save()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg="Testando se o padrao do steps is html não é Falso",
        )
