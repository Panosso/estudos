import pytest
from bytebank import Funcionario


# Boas praticas para tests e leitura
class TestClass:
    #Nome da função tem que ser o mais verbose possivel
    def test_quando_idade_receber_15_12_1991_deve_retorna_32(self):
        #Given
        entrada = '15/12/1991'
        esperado = 33

        funcionario_teste = Funcionario('Teste', entrada, 7777)

        #When
        resultado = funcionario_teste.idade()

        #Then
        assert resultado == esperado

    def test_quando_nome_receber_pedro_machado_deve_retornar_machado(self):
        entrada = 'Pedro Machado'
        esperado = 'Machado'

        funcionario_teste = Funcionario(entrada, '15/12/1991', 7777)

        assert funcionario_teste.sobrenome() == esperado


    def test_quando_diminuir_salario_recebe_10000_retorna_9000(self):
        entrada = 10000
        esperado = 9000

        funcionario_teste = Funcionario('Teste', '15/12/1991', 10000)
        funcionario_teste.subtrair_salario(1000)

        assert funcionario_teste.salario == esperado

    #É possivel executar tests que possuam determinada tag, utilizando o mark.
    # Utilizando o comando pytes -v -m <tag>, nosso exemplo seria calcular_bonus
    # Existem mark's padronizados, que podem ser consultados em:
    # pytest.exe --markers
    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_retorna_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '15/12/1991', entrada)
        funcionario_teste.aumento_salarial()

        assert funcionario_teste.aumento_salarial() == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_retorna_100_exceptions(self):
        #Indico para o test que o esperado de resultado é uma exception
        with pytest.raises(Exception):
            entrada = 1000000000

            funcionario_teste = Funcionario('Teste', '15/12/1991', entrada)
            funcionario_teste.aumento_salarial()

            # O assert vai conferir que o resultado será uma excessão, como esperado e indicado.
            assert funcionario_teste.aumento_salarial()

    # def teste_dunder_str_retorna_teste_15_12_1991_1000(self):
    #     esperado = 'Funcionario: Teste, Nasceu: 15/12/1991, Salario: 10001'
    #     funcionario_teste = Funcionario('Teste', '15/12/1991', 10001)

    #     assert esperado == funcionario_teste.__str__()

    # #Feito para o test falhar
    # def test_vai_falhar(self):
    #     assert 2 == 1

    # #Feito para o test nao rodar
    # def O_test_que_nao_vai_rodar(self):
    #     assert 1 == 1
