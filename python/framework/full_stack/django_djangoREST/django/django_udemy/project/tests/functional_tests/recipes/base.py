#Sobe um servidor de testes com arquivos estaticos.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from recipes.tests.test_recipe_base import RecipeMixin

class RecipeBaseFuncTest(StaticLiveServerTestCase, RecipeMixin):

    def setUp(self):
        self.browser = make_chrome_browser()
        return super().setUp()
    
    def tearDown(self):
        self.browser.quit()
        return super().tearDown()