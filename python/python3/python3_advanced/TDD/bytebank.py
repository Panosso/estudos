from datetime import date

class Funcionario:

    def __init__(self, nome_completo, data_nascimento, salario):
        self._nome = nome_completo
        self._salario = salario
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario
    
    def idade(self):
        data_nascimento_broke = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_broke[-1]
        ano_atual = date.today().year
        print(ano_atual - int(ano_nascimento))
        return ano_atual - int(ano_nascimento)
    
    def sobrenome(self):
        nome_completo = self._nome.strip().split(' ')
        return nome_completo[-1]

    def calcular_bonus(self):
        valor = self._salario * 0.1
        return
    
    def subtrair_salario(self, valor):
        self._salario = self._salario - valor

    def aumento_salarial(self):
        valor = self._salario * 0.1
        if valor > 100:
            raise Exception('O salário mto alto para receber bonus')
        return valor

    def __str__(self):
        return f'Funcionario: {self._nome}, Nasceu: {self._data_nascimento}, Salario: {self._salario}'
