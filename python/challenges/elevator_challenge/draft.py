UP = 0
DOWN = 1
IDLE = 2

summon_demand = {UP: set(), DOWN: set()}

summon_demand[UP].add(123)

print(len(summon_demand[UP]))
print(summon_demand[UP])
print(type(summon_demand[UP]))
print(type(summon_demand[UP]))