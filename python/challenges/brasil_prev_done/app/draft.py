import hashlib
import random
import re
from datetime import datetime
from math import floor


def susep(susep) -> bool:
    if re.match(r'15414.6\d{5}/\d{4}-\d{2}', susep):
        print(True)
    else:
        print(False)


def email_validator(email) -> bool:

    r = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    valid = re.match(r, email)

    return bool(valid)


data1 = datetime.now().date()
data2 = datetime(1991, 12, 15).date()
diff = data1 - data2
print(diff.days)
diff = diff.days/365

data3 = datetime.strptime('2000-01-01', '%Y-%m-%d').date()

print(data1)
print(data2)
print(data3)
print(floor(diff))

email = 'pedro@gmail.com'
flt_val = 1
print(email_validator(email))

print(hash(flt_val))

susep('15414.6XXXXX/AAAA-DV')
susep('15413.612345/1234-3A')
susep('15414.612345/1234-32')
susep('1544.612345/1234-3A')
susep('15414.612345/1234-DV')


x = random.randint(1, 52)

str2hash = "GeeksforGeeks"

result2 = hashlib.md5(str2hash.encode()).hexdigest()

print(result2)

data_expira = datetime.strptime('2002-01-01', '%Y-%m-%d').date()
data_compra = datetime.strptime('2001-01-01', '%Y-%m-%d').date()

teste = True if data_compra < data_expira else False

print(teste)

agora = datetime.now()

print(''.join([x for x in str(agora) if x.isdigit()]))

result2 = hashlib.md5(
    ''.join([x for x in str(agora) if x.isdigit()]).encode()).hexdigest()

print(result2)
