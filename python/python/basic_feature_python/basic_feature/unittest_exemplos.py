#teste.py
import unittest

from teste_geral_unittest import comer, dormir

class Teste_geralTestes(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(comer('quiabo', True), 'Estou comendo quiabo porque quero')
        self.assertEqual(comer(comida='pizza', eh_saudavel=False), 'Estou comendo pizza pq sim')
    

if __name__ == '__main__':
    unittest.main()
