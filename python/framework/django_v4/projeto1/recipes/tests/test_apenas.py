from django.test import TestCase


class ApenasTest(TestCase):
    def test_the_pytest_is_ok(self):
        print("Ola Mundo")
        assert 1 == 1, "Um é igual a um"
