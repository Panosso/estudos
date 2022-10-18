import timeit

print('-'.join(str(n) for n in range(100)))

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=1000))

print(timeit.timeit('"-".join(map(str, range(100)))', number=1000))
