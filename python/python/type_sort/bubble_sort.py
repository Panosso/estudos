from random import randint
import time

#starting time
start = time.time()

value_list = [randint(-1000, 1000) for _ in range(1000)]

def bubble_sort(value_list):
    n = len(value_list)

    for i in range(n):

        for j in range(0, n-i-1):

            if value_list[j] > value_list[j+1]:

                value_list[j], value_list[j+1] = value_list[j+1], value_list[j]

    return value_list

end = time.time()

print("Execution time of the program is: ", end-start)
print(f"List sorted: {bubble_sort(value_list)}")
