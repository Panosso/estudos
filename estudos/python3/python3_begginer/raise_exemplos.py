def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Tipo errado da variavel')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
        
    if cor not in cores:
        raise ValueError(f'Precisa ser uma dessas cores {cores}')
        
    print(f"O {texto} será impresso na cor {cor}")


colore('Batatinha azul', 'azul')
