my_dic = {'nome':'Pedro',
        'idade': 28,
        'habilidades': ['aws', 'linux', 'python']}

print(my_dic)
print(my_dic['nome'])
print(my_dic['habilidades'][0])

my_dic['nome'] = 'Jaque'

print(my_dic)

my_dic = {}

my_dic['nome'] = 'Pedro'

my_dic['idade'] = 28

print(my_dic)

#Atualizando um dicionário
novo_dado = {'peso': 120}

my_dic.update(novo_dado)

my_dic = {'nome': 'Pedro',
'idade': 28,
'habilidades': ['aws', 'linux', 'python'], 
(120, 321): 'Gordo pra caralho'}}

#Outros modos de criar um dicionário mais recomendado
my_dic2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
my_dic3 = {}.fromkeys('a', 'b')

#Um jeito de criar várias chaves com o mesmo valor,
#Nesse exemplo será criado as chaves a,c,d,e todas elas com o valor b
my_dic4 = {}.fromkeys(['a', 'c', 'd', 'e'], 'b')
my_dic5 = {}.fromkeys(range(0,11,1), 'b')

#retorna as chaves do dicionario
print(my_dic.keys())

#retorna os valores do dicionario
print(my_dic.values())

#retorna todo o dicionario
print(my_dic.items())

#Recomendado recuperar o valor de um dicionario com o method get
print(my_dic2.get('br'))
print(my_dic.get((120,321)))

#Verifica se um valor está no dicionario
print('br' in paises) #True
print('GB' in paises) #False

# {Chave:valor}
d = {x:x**2 for x in range(100)}


numeros = [1,2,3,4,5]

print({numero:('par' if numero % 2 == 0 else 'impar') for numero in numeros})
