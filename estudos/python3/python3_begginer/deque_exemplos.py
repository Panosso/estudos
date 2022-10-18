from collections import deque


deq = deque('Pedro')

#deque(['P', 'e', 'd', 'r', 'o'])
print(deq)

deq.append('y')

#deque(['P', 'e', 'd', 'r', 'o', 'y'])
print(deq)

#deque(['K', 'P', 'e', 'd', 'r', 'o', 'y'])
deq.appendleft('K')
print(deq)

#y
print(deq.pop())

#deque(['K', 'P', 'e', 'd', 'r', 'o'])
print(deq)

#K
print(deq.popleft())

#deque(['P', 'e', 'd', 'r', 'o'])
print(deq)
