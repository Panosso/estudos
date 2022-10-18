#exemplo thread        
import time
from threading import Thread

contador = 5000000

def contagem(n):
    while n > 0:
        n -= 1
        
inicio = time.time()
contagem(contador)
fim = time.time()

print(f'Tempo em segundos {fim - inicio}')
        
t1 = Thread(target=contagem, args=(contador//2, ))
t2 = Thread(target=contagem, args=(contador//2, ))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
