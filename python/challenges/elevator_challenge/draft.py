UP = 1
DOWN = 2

dicta = {UP: set(), DOWN: set()}

a = [5, 2, 6, 3, 0]

demand = len(set([len(dicta[k]) for k in dicta]))

print(demand)

print(dicta[UP])

dicta[UP] = set()

dicta[UP].add(2222)
dicta[UP].add(22222)
dicta[UP].add(22322)
dicta[UP].add(2222)
dicta[UP].add(22522)
dicta[UP] = set()
print(any(dicta.values()))

target_floors = []

if target_floors:
    print('Aqui')