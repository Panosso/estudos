# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
from string import Template
import itertools
import collections
from enum import Enum, auto


def print_hi(name):

    def condition(x):
        return x < 40

    #Difference between string and byte
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"

    print(s)

    #Objects string and bytes can not be concatenate
    #print(s + b)

    #Decode transform bytes into string, so now you can concatenate.
    print(s + b.decode('utf-8'))

    #Encode transform string into byte
    print(s.encode('utf-32') + b)

    phrase = "You're watching {0} with {1}".format("Python Advanced", "Pedro Panosso")
    print(phrase)

    #Templates
    templ = Template("You're watching ${curso} with ${instrutora}")

    #Using substitute method
    phrase2 = templ.substitute(
        curso = "Python Advanced",
        instrutora = "Pedro Panosso"
    )
    print(phrase2)

    #Using dictionary
    templ = Template("Voce ${nome} tem ${idade} anos")
    d = {"nome": "Pedro", "idade": 23}
    phrase3 = templ.substitute(d)
    print(phrase3)


    #Using iter and next function with list
    days_pt_br = ["DOM","SEG","TER","QUA","QUI","SEX","SAB"]
    iter_days_pt_br = iter(days_pt_br)
    print(next(iter_days_pt_br))
    print(next(iter_days_pt_br))
    print(next(iter_days_pt_br))
    print(next(iter_days_pt_br))

    #Using iter and next with file
    with open('exemple_iter.txt', 'r') as f:
        for line in iter(f.readline, ''):
            print(line)

    #Using enumerate
    for i, day in enumerate(days_pt_br):
        print(i, day)

    #Itertools
    #Cycle - This iter, restart the list when he reach the last element
    people = ["Pedro", "Yago", "Zaque"]
    p = itertools.cycle(people)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))


    #Count - Iter count, start and step
    iter_count = itertools.count(100, 10)
    print(next(iter_count))
    print(next(iter_count))
    print(next(iter_count))
    print(next(iter_count))
    print(next(iter_count))
    print(next(iter_count))

    #Accumulate - Iter tool who acumulate values, step by step
    values = [10, 20, 30, 39, 20, 600, 40, 50, 40, 30, 10]
    accumulated = itertools.accumulate(values)
    print(next(accumulated))
    print(next(accumulated))
    print(next(accumulated))
    print(next(accumulated))
    print(next(accumulated))
    #Return a list of sum by te formula (n + n-1)
    print(list(itertools.accumulate(values)))
    #In this exemple, when the accumulate function find the higher value, the other values will be assume thar value
    #[10, 20, 600, 600, 600, 600, 600]
    print(list(itertools.accumulate(values, max)))

    #Chain - Iter tool who return each element by the element in argument
    x = itertools.chain("ABCD", "1234", values, people, phrase3)
    print(list(x))


    #DropWhile and TakeWhile - pass a condition and a list of values
    #DropWhile will drop value from a list, until he find some value that satisfy the condition, and return all values after this.
    print(list(itertools.dropwhile(condition, values)))

    #TakeWhile will get all values until he find some value that satisfy the condition, and return all values after before this.
    print(list(itertools.takewhile(condition, values)))

    #In this function the param with * must be a list
    def mult_param_function(*args):
        return sum(args)

    print(mult_param_function(5,2,3,4,5,6))
    print(mult_param_function(*values))


    #namedtuple
    coordinate = collections.namedtuple("Coordinate", "x y")

    p1 = coordinate(10, 20)
    p2 = coordinate(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)

    p1 = p1._replace(x=100)
    p1 = p1._replace(y=50)
    print(p1.x, p1.y)


    #Default dict -> Create a dictionary with a default value if the key is not exist
    fruits_dict = collections.defaultdict(lambda: 0)
    fruits = ["apple", "banana", "pineapple", "orange", "lemon", "apple", "apple", "banana"]
    for i in fruits:
        fruits_dict[i] += 1

    print(fruits_dict)

    #Counter
    team_a = ["Pedro", "Jaque", "Yago", "Manoel", "Joaquim", "Pedro"]
    team_b = ["Pedro", "Jose", "Jaque", "Yago", "Manoel", "Joaquim", "Jose"]

    a = collections.Counter(team_a)
    print(a["Pedro"])
    print(sum(a.values()))

    a.update(team_b)
    print(a)

    print(a.most_common())

    #Deque
    letters = collections.deque(string.ascii_lowercase)
    # print(len(letters))
    # for letter in letters:
    #     print(letter.upper(), end=', ')

    letters.pop()
    letters.popleft()
    letters.append(2)
    letters.appendleft(1)
    print(letters)

    letters.rotate(10)
    print(letters)

    #Enum
    class Fruit(Enum):
        GRAPPE = 1
        BANANA = 2
        APPLE = 3
        ORANGE = 4
        TOMATE = auto()

    f1 = Fruit.TOMATE
    print(f1)
    print(type(f1))
    print(repr(f1))
    print(f1.name, f1.value)

    fruits = dict()
    fruits[Fruit.BANANA] = "Yellow"
    print(fruits[Fruit.BANANA])

    #Class Representation
    class Person():
        def __init__(self):
            self.nome = "Pedro"
            self.sobrenome = "Panosso"
            self.idade = 29

        def __repr__(self):
            text = f"<Class person - dunder repr method - name: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}>"
            return text

        def __str__(self):
            text = f"<Class person - dunder str method - name: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}>"
            return text

        def __bytes__(self):
            text = f"<Class person - dunder bytes method - name: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}>"
            return text.encode('utf-8')

    p = Person()
    print(p)
    print(repr(p))
    print(bytes(p))


    class MyColor():

        def __init__(self):
            self.red = 100
            self.green = 50
            self.blue = 23


        #Call this item, in this exemple, the item value is 'rgb'
        def __getattr__(self, item):
            if item == "rgb":
                return (self.red, self.green, self.blue)
            else:
                raise AttributeError


        def __setattr__(self, key, value):
            if key == "rgb":
                self.red = value[0]
                self.green = value[1]
                self.blue = value[2]

            else:
                super().__setattr__(key, value)

        def __dir__(self):
            return ("red", "green", "blue", "rgb")

    c = MyColor()
    print(c.rgb)
    c.rgb = (10,20,30)
    print(c.rgb)
    print(dir(c))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
