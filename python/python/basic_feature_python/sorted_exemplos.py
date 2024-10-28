tupla = (3,4,5,6,2,7,1,2,7)

lista = [3,4,5,6,2,7,1,2,7]

my_dic = {'nome':'Pedro',
        'idade': 28,
        'habilidades': ['aws', 'linux', 'python']}

#Ordena normal
print(sorted(tupla))

#Ordena de forma reversa
print(sorted(lista, reverse=True))

#define uma chave para ordenar
print(sorted(my_dic, key=len))
