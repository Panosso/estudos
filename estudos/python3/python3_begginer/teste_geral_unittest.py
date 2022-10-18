#teste_geral_unittest.py
def comer(comida, eh_saudavel):
    
    if eh_saudavel == True:
    
        return f'Estou comendo {comida} porque quero'
    
    elif eh_saudavel == False:
        
        return f'Estou comendo {comida} pq sim'
    
def dormir(num_horas):
    pass

import unittest

from teste import Robo

class TesteRobo(unittest.TestCase):
    
    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print("SetUp sendo executado...")
    
    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'Meu nome é MEGA MAN')

    def tearDown(self):
        print('tearDown() sendo executado...')

if __name__ == '__main__':
    unittest.main()
