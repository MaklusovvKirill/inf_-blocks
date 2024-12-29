s = 14
print(s)
k = -3
print(k)
try:
    d = s + 1
    print(d)
except NameError as e:
    print(e)

s = d
print(s)
try:
    k = 2 * s
    print(k)
except NameError as e:
    print(e)


s = 0
print(s)

k = 30
print(k)
try:
    d = k - 5
    print(d)
except NameError as e:
    print(e)

try:
    k = 2 * d
    print(k)
except NameError as e:
    print(e)


try:
    s = k - 100
    print(s)
except NameError as e:
    print(e)
