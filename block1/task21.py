a = 5.8
print(a)
b = -7.9
print(b)
try:
    b = a
    print(b)
except NameError as e:
    print(e)

try:
    a = b
    print(a)
except NameError as e:
    print(e)


a = 0
print(a)
b = -9.99
print(b)
try:
    b = a
    print(b)
except NameError as e:
    print(e)

try:
    a = b
    print(a)
except NameError as e:
    print(e)
