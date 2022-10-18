#Assert exemple
a = 10

b = 12

assert a > b, 'Burro'

print("Fim.")

def comidas(comida):
    assert comida in ['pizza', 'sorvete', 'doces', 'batata', 'cachorro'], 'A comida tem que ser fast food'
    return f'Eu estou comendo {comida}'


print(comidas('sorvete'))
