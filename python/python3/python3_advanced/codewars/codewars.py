# def title_to_number(title):

#     alfa = 'abcdefghijklmnopqrstuvwxyz'

#     dicionario = dict([(x[1],x[0]+1) for x in enumerate(alfa)])

#     resultado = 0
#     contador = 0

#     if len(title) == 1:
#         resultado += dicionario[title.lower()]

#     else:
#         for i in reversed(title):
#             contador += 1
#             print(contador)
#             resultado += dicionario[i].lower() + (26*contador)
#             sleep(5)

# #posicao alfabeto + 26*posicao albateo*posiçãostring...n vezes
            
#     return resultado


# print(title_to_number('Z') == 26)
# print(title_to_number('AA') == 27)
# # print(title_to_number('BA') == 53)
# # print(title_to_number('AAA') == 703)
# # print(title_to_number('CODEWARS') == 28779382963)

# #Para cada letra da direita para a esquerda, calcular o valor dela será isso...
# #posição dela no alfabeto + * posição dela na string 

n1 = input('Digiete')
print(type(n1))

print(help(max))