#teste.py
class Robo:
    
    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades
        
    @property
    def nome(self):
        return self.__nome

    @property    
    def bateria(self):
        return self.__bateria
    
    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        print('carregar')
        self.__bateria = 100
    
    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Meu nome é {self.__nome.upper()}'
        return f'Sem bateria, recarrega ae arrombado'

    def aprender_habilidade(self, custo, nova_habilidade):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'uau sou foda, aprendi {nova_habilidade.upper()}'
            
        return f'Sem bateria, recarrega ae arrombado'
