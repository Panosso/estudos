from sys import getsizeof

list_comprehension = getsizeof([num for num in range(10)])
set_comprehension = getsizeof({num for num in range(10)})
dic_comprehension = getsizeof({num: num * 10 for num in range(10)})
generator = getsizeof((num for num in range(10)))

print('Para fazer a mesma coisa cada tipo de método utiliza uma certa quant de memória')
print(f'List Comp: {list_comprehension} b')
print(f'Set Comp: {set_comprehension} b')
print(f'Dic Comp: {dic_comprehension} b')
print(f'Generator: {generator} b')
