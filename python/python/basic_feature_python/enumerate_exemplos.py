#syntax: enumerate(lista)

lst = ['a', 'b', 'c']

#[(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(lst)))


#0:a
#1:b
#2:c
for number, item in enumerate(lst):
    print(str(number) + ':' + str(item))