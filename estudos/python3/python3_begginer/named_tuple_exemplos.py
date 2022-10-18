from collections import namedtuple

#3 jeitos de declarar uma namedtuple
Dog = namedtuple('Dog', 'age breed name')
#Dog = namedtuple('Dog', 'age, breed, name')
#Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sam = Dog(age=10, breed='Huskei', name="Sam")

print(sam)
print(sam.name)
print(sam[0])
