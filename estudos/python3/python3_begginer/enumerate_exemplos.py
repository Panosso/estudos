dic1 = {'a':1, 'b':2}
dic2 = {'c':3, 'd':4}

#Combinando chave e valor dos 2 dic
print(list(zip(dic1.items(), dic2.items())))

#Combinando valor dos 2 dic
print(list(zip(dic1.values(), dic2.values())))
