from random import randint
import time

#starting time
start = time.time()

value_list = [randint(-1000, 1000) for _ in range(1000)]

def sort_algorithm(value_list):
    pass

end = time.time()

print("Execution time of the program is: ", end-start)
print(f"List sorted: {sort_algorithm(value_list)}")