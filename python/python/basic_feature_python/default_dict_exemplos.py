from collections import defaultdict

d = defaultdict(lambda: 0)

d['one'] = 'Teste'

#defaultdict(<function <lambda> at 0x7fbfde3c1a70>, {'one': 'Teste'})
print(d)

#0
print(d['40edoze'])

#defaultdict(<function <lambda> at 0x7fbfde3c1a70>, {'one': 'Teste', '40edoze': 0})
print(d)
