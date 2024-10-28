import re

patters = ["term1", "term2"]

text = 'This is a string with a term1, this is another with term2'

print(re.search(patters[0], text))


match = re.search(patters[0], text)

#Alguns metodos do re quando ele encontra um padrao
print(match.start())
print(match.end())
