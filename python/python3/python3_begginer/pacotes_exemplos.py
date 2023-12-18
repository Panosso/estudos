from panosso import (
matematica,
gramatica,
machado
)

from panosso.machado import (
geografia,
historia
)

#Todos os comando são referentes ao primeiro import.
print(matematica.soma(1,2))
print(gramatica.curso_nome())
print(machado.geografia.pedra())
print(machado.historia.navegador())

#Todos os comando são referente ao segundo import.
print(geografia.pedra())
print(historia.navegador())
