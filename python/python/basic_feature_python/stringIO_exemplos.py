from io import StringIO

message = 'This is a normal string'

f = StringIO(message)

print(f.read())

f.write("\n mais uma linha")

f.seek(0)

print(f.read())
