#from passlib.hash import pbkdf2_sha256

class ContaCorrente:
    
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    
    contador = 0
    
    #O parametro cls é a propria classe.
    #Portanto estamos fazendo o seguinte:
    #Estamos printando o valor de Usuario.classe
    #Por convenção o parâmetro é chamado de cls apreviação de class
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')
    
    @staticmethod
    def definicao():
        return f'batata'
    
    def __init__(self, nome, email, senha):
        self.id = Usuario.contador + 1
        self.nome = nome
        self.email = email
        self.senha = senha
        #self.senha = pbkdf2_sha256.hash(senha)
        Usuario.contador = self.id
        print(f'Email splitado: {self.__gera_usuario()}')
        print("\n\n\n\n\n")
        
    #def checa_senha(self, senha_digitada):
    #    if pbkdf2_sha256.verify(self.senha, senha_digitada):
    #        return f'Voce logou'
    #    
    #    return f'Senha errada'
    
    
    #Esse método só pode ser acessar dentro da classe.
    def __gera_usuario(self):
        return self.email.split('@')[0]

class Produto:

    #Atributos de classe
    imposto = 1.05
    __qtd_controles = 4
    contador = 0

    def __init__(self, nome, descricao, valor):
        #Atributos de instancia
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
        
    def desconto_porcentagem(self, desconto):
        return (self.valor * (100 - desconto)/100)

class Lampada:
    
    #Atributos com '__' são atributos privados, ou seja, eles só podem ser modificados dentro da classe
    def __init__(self, voltagem, cor, marca='Padrao'):
        self.marca = marca
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    #Para poder alterar o valor da voltagem descomentar esse método
    #@property
    #def voltagem(self):
    #    return self.__voltagem

    @property
    def cor(self):
        return self.__cor
        
    @property
    def ligada(self):
        return self.__ligada


#Instanciando classes.
usuario = Usuario('Pedro', 'pedropanosso@gmail.com', '!@#qwe456')
lamp = Lampada(127, 'amarela')
ps4 = Produto('Ps4', 'Melhor video game', 200)
xbox = Produto('XBOX', 'Pior video game', 1)


#Acessando uma variável privada
print("Acessando uma vairavel privada")
print(Produto._Produto__qtd_controles)
print("\n\n\n\n\n")

#Posso acessar as variaveis da classe
print("Variaveis da classe")
print(Produto.imposto)
print(ps4.id)
print(ps4.nome)
print(ps4.valor)
print(xbox.id)
print("\n\n\n\n\n")

#Atributo Dinâmico.
print("Atributo dinâmico")
ps4.peso = '5kg'
print(ps4.peso)
print("\n\n\n\n\n")

#Retorna um dicionário onde a chave é o nome da variavel e o valor é o valor da variavel. Apenas do construtor da classe.
print("Dicionário da classe")
print(ps4.__dict__)
print("\n\n\n\n\n")

#Deletando um atributo
print("Atributos deletados.")
del ps4.peso
del ps4.nome
print(ps4.__dict__)
print("\n\n\n\n\n")

#Acessando o método pelo objeto
print("Acessando o método pelo objeto")
print(ps4.desconto_porcentagem(10))

#Acessando o método pela classe passando um objeto do mesmo tipo, que será atribuido ao self.
print("Acessando o método pela classe")
print(Produto.desconto_porcentagem(ps4, 10))
print("\n\n\n\n\n")

#Imprimindo o valor da variavel senha da classe Usuário
print("Acessando o valor do atributo")
print(usuario.senha)

#Erro
#print(usuario.__gera_usuario())
print("\n\n\n\n\n")

#Acesso ao metodo "privado", porem nao recomendado.
print("Acessando método 'privado'")
print(usuario._Usuario__gera_usuario())

#print(Usuario.checa_senha("!@#qwe456")) #Acessa
#print(Usuario.checa_senha("dhusadhusa")) #Nao acessa
Usuario.conta_usuario() #Forma correta
usuario.conta_usuario() #Forma errada

#Acessando o método estático da clsse
print("Acessando o método estático")
print(usuario.definicao())
print("\n\n\n\n\n")

print("Acessando o atributo")
print(lamp.marca)
print(dir(lamp))

#Método para acessar uma variavel 'privada' dentro da classe
print("Acessando uma variavel 'privada'")
print(lamp._Lampada__cor)
print("\n\n\n\n\n")

#Alterando o valor de uma atributo
print("Alterando o valor do atributo")
lamp.marca = 'Outra'

print(lamp.marca)
print("\n\n\n\n\n")

#Erro pois eu nao consigo alterar o atributo.
lamp.voltagem = 220

#panosso.py
class PrimeiraClasseFracamentePrivada():

    def __init__(self):
        self._atributoFracamentePrivado = 123456


    def _primeiroMetodoFracamentePrivado(self):
        print("Metodo inutil")


class PrimeiraClassFortementePrivada():


    def __init__(self):
        self.__atributoFrotementePrivado = 520741


    def __primeiroMetodoFrotementePrivado(self):
        print("método fortemente privado")


# Dog
class Dog(object):

    # essa variavel é utilizada na classe toda e pode ser acessada normalmente, nesse exemplo, todo cachoro é mamifero
    especie = "mamífero"

    # o atributo self está dizendo que a variavel é da classe Dog, portanto quando atribuimos o valor self.raca,
    # estamos dizendo que a classe Dog tem uma variavel chamada raca e ela é igual a raca
    # o self é passado automático na quando a classe é instanciada
    # sempre que definimos uma variável nesse init podemos acessa-lo pelo operador '.'
    def __init__(self, raca, nome):
        # pode ser um nome qualquer, desde que esteja declarado como atribudo da funcao __init__
        self.raca = raca
        self.nome = nome
        self.numcharact = len(self.especie)

    #Metodo
    def latir(self, cachorro):
        self.cachorro = cachorro
        print("O cachorro %s latiu" % (cachorro))

    #Metodo só com o self
    def latir_2(self):
        print("Au Au")

# Circulo
class Circle(object):
    pi = 3.14

    #caso nao seja passado nenhum valor para o radius ele iniciara como 1
    #porém se for instanciada a classe como Circle(radius=2) o radius terá o valor 2
    def __init__(self, radius=1):
        self.radius = radius

    #altera o valor do radius
    def setRadius(self, radius):
        self.radius = radius

    #Calcula a area do circulo
    def area(self):
        return (self.radius ** 2) * self.pi

    #Pega o valor atual do raio
    def getRadius(self):
        return self.radius


class Sample(object):

    def __init__(self, texto="Entrei no init"):
        self.texto = texto


class Automovel(object):

    def __init__(self, motor="2.0", velocidade_max=100, velocidade_min=10, nome='Faltou o nome'):
        self.motor = motor
        self.velocidade_max = velocidade_max
        self.velocidade_min = velocidade_min
        self.nome = nome
        print("Automovel criado")

    def velocidade(self):
        return "Velocidade Max: %i \nVelocidade Min: %i" %(self.velocidade_max, self.velocidade_min)

    def informacoes(self):
        return "Motor %s \nVelocidade Max %i\nVelocidade Min %i" %(self.motor, self.velocidade_max, self.velocidade_min)

#Carro herda atributos da classe automovel e circle
class Carro(Automovel, Circle):

    def __init__(self, marca, cor, qtd_pneu):
        #Permite carregar os dados do init da class Automovel
        Automovel.__init__(self)
        Circle.__init__(self)
        self.marca = marca
        self.cor = cor
        self.qtd_pneu = qtd_pneu
        print("Carro Criado")

    def informacoes_carro(self):
        return "A marca é: %s\n Cor: %s\n E tem %i pneus" \
            " ele tem motor %s e velocidade max e min %i, %i" \
            " respectivamente" %(self.marca, self.cor, self.qtd_pneu, self.motor, self.velocidade_min, self.velocidade_max)

    def informacoes(self):
        return "Marca %s, Cor %s, qtd_pneu %i" %(self.marca, self.cor, self.qtd_pneu)

class Book(object):

    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
    #Quando printamos uma variavel com esse objeto criado, o return dessa funçao é o que será impresso
    def __str__(self):
        return "Titulo {a}".format(a=self.titulo)

    #Retorna o tamanho de paginas apenas para esse funcao
    def __len__(self):
        return self.pagina

    #Destroi o objeto e entao printa que "Livro Destruido"
    def __del__(self):
        print("Livro destruido")

                        
#main.py
            
#from panosso import PrimeiraClasseFracamentePrivada as fraco
#from panosso import PrimeiraClassFortementePrivada as forte
from panosso import Dog
from panosso import Circle
from panosso import Sample
from panosso import Automovel
from panosso import Carro
from panosso import Book

#p1 = fraco()
#
#p1._primeiroMetodoFracamentePrivado()
#
#print(p1._atributoFracamentePrivado)
#
#p2 = forte()
#
#p2.__primeiroMetodoFrotementePrivado()
#print(p2.__atributoFrotementePrivado)

x = Sample()
c = Circle(radius=2)
frank = Dog("Labra", "Frank")
sam = Dog("Xiuaua", "Sam")

#Quando instanciada será impresso o que está no print dessas classes
auto = Automovel("2.0 flex", 200, 10, "Monstro")
car = Carro("Toiota", "Preto", 4)
livro = Book("A volta dos que nao foram", "Minha Pika", 100)


#Variaveis relacionadas ao Samples
print(type(x))
print(x.texto)
print(10*'-')

#Variaveis relacionadas a classe Dog ao cachorro sam
print(sam.nome) #acessando o variavel nome que está dentro da class Dog
print(sam.raca)
print(sam.especie)
print(Dog.latir(sam, sam.nome))
print(sam.latir_2())
print(sam.numcharact)
print(10*'-')

#Variaveis relacionadas a classe Dog ao cachorro Frank
print(frank.nome)
print(frank.raca)
print(frank.especie)
print(Dog.latir(frank, frank.nome))
print(frank.numcharact)
print(10*'-')

#Classe Circulo
print(c.getRadius())
c.setRadius(10)
print(c.getRadius())
print(c.area())

#Automovel
print(10*'-')
print(auto.nome)
print(auto.motor)
print(auto.velocidade_min)
print(auto.velocidade_max)
print(auto.velocidade())
print(auto.informacoes()) #Vai printar o metodo informacoes da classe automovel

#Carro
print(10*'-')
print(type(car))
print(type(auto))
print(car.informacoes_carro())
print(car.velocidade())
print(car.informacoes()) #Vai printar o metodo informacoes da classe carro

#Book
print(livro)
print(len(livro))
del livro


#Outro Exemplo
from panosso import Gerente

gerente = Gerente('Pedro', '77120272853', '2500', 'Panosso1512', 10, '100')

print(gerente.imprimir_tudo())
print(gerente.imprimir_tudo2())


#classo exemplo 2
class Funcionario(object):

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = str(cpf)
        self.salario = salario

    def imprimir_tudo(self):
        return self.nome + str(self.salario) + self.cpf

class Funcionario2(object):

    def __init__(self, tamanho):
        self.tamanho = tamanho

    def imprimir_tudo2(self):
        return self.tamanho

class Gerente(Funcionario, Funcionario2):

    def __init__(self, nome, cpf, salario, senha, qts_gerenciados, tamanho):
        super().__init__(nome, cpf, salario)
        self.tamanho = tamanho
        self.senha = senha
        self.qts_gerenciados = qts_gerenciados

    def autenticar(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True

        else:
            print("Acesso negado")
            return False

class Pessoa(object):
    def __init__(self, nome, sobrenome, cpf):
        #Atributos privados.
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, renda:float):
        #Acessa o contrutor da superclasse (Pessoa)
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, matricula):
        #Acessa o contrutor da superclasse (Pessoa), nesse exemplo é passado o nome do classe que é herdada
        # portanto é necessário passar o 'self' como parametro
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        #Acessando o método nome_completo da classe Pessoa
        print(super().nome_completo())
        
        return f'Matricula: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Pedro', 'Panosso', '40149796870', 5000)
funcionario1 = Funcionario('Pedro', 'Panosso', '40149796870', 123321)

print(cliente1.nome_completo())

#{'_Pessoa__nome': 'Pedro', '_Pessoa__sobrenome': 'Panosso', '_Pessoa__cpf': '40149796870', '_Cliente__renda': 5000}
print(cliente1.__dict__)

print(funcionario1.nome_completo())

class Conta:
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        self.__saldo -= valor
        
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
        
    @property
    def numero(self):
        return self.__numero
        
    @property
    def titular(self):
        return self.__titular
        
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
        
    #Criando uma nova propriedade, sendo que esse valor_total nao foi declarado no construtor da classe
    @property
    def valor_total(self):
        return self.__saldo + self.__limite
        
    @saldo.setter
    def saldo(self, novo_valor):
        self.__limite += novo_valor


conta1 = Conta("Pedro", 1555, 5000)
conta2 = Conta("Zaque", 1000, 6000)

#Não é necessário os () pq o proprio decorator já sabe trabalhar sem eles
print(conta1.limite)
print(conta1.saldo)

#Não é necessário passar os () pois o decorator sabe trabalhar com o valor da variavel.
print(conta1.saldo)
print(conta1.valor_total)

class Animal:
    
    def __init__(self, nome, especie):
        self.__nome = nome
        self.especie = nome
        
    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')
        
class Gato(Animal):
    
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)

        #Acessando o método pelo super
        super().faz_som('Miau')
        self.__raca = raca
        

pantera = Gato('Pantera', 'felino', 'pocalia')

pantera.faz_som('Miau')

#Polimorfismo
class Animal(object):
    
    def __init__(self, nome):
        self.__nome = nome
        
    def falar(self):
        raise NotImplementedError("A classe filha tem que implementar")
        
    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self._Animal__nome} falou')

class Gato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self._Animal__nome} falou')

class Rato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        

c = Cachorro('Dogao')
g = Gato('Galeon')
r = Rato('Jerry')

c.falar()
c.comer()

g.falar()
g.comer()

r.comer()
r.falar()

#Métodos mágicos

#__str__ --> Representação do objeto

#__repr__ --> Representação do objeto, igual ao __str__, porém se o __str__ for declardo o código não vai procurar pelo __repr__, ao menos que o método seja chamado

#__len__ --> Retorna um número intero, geralmente relacionado a quantidade de paginas ou quantidade de caracteres ou itens em uma lista

#__del__ --> Deleta um objeto

#__add__ --> Somatória

#__mul__ --> Multiplicacao

class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f'{self.titulo} escrito por {self.autor} no str'
        
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor} no repr'
        
    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Livro {self.titulo} deletado')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self) + '\n'    
            return msg
        return 'Não posso multiplicar' 
    
l1 = Livro("Python", "Eu", 110)
l2 = Livro("Ia", "Ele", 1110)

print(l1)
print(l1.__repr__())
print(len(l1))

#Nessa soma ele vai chamar o método __str__ portanto a conta seria l1.__str__() - l2__str__()
print(l1 + l2)

print(l1 * 3)

del l1
