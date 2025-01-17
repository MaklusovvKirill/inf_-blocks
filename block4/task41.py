import math

x = int(input("Введите число x"))


def f(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1


x = float(input("Введите вещественное число x: "))
result = f(x)
print(f"f({x}) = {result}")


def f(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1


x = float(input("Введите вещественное число x: "))
result = f(x)
print(f"f({x}) = {result}")
