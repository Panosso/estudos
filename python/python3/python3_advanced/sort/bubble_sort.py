lista = [8,10,3,2,5,4,9,6]

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):

        for j in range(0, n-i-1):

            if lista[j] > lista[j+1]:

                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

print(bubble_sort(lista))
