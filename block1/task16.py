from math import sin, radians, sqrt, cos
x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
d = int(input("Введите число d: "))
abs = int(input("Введите число s: "))
R = int(8.31446261815324)

A = (f'{a / b / c}')
B = (f'{a * b / c}')
V = (f'{a / b * c}')
G = (f'{a + b / c}')
D = (f'{(a + b) / c}')
E = (f'{a + b / b + c}')
ZH = (f'{(a + b) / (b + c)}')
Z = (f'{a / sin(radians(b))}')
I = (f'{1 / 2 * a * b * sin(radians(x))}')
K = (f'{2 * b * c * cos(radians(a / 2) / (b + c))}')
L = (f'{4 * R * sin(radians(a / 2)) * sin(radians(b / 2)) * sin(radians(c / 2))}')
M = (f'{a * x + b / (c * x * d)}')
N = (f'{2 * sin(radians(a + b)) / 2 * cos(radians((a - b) / 2))}')
O = (f'{abs * 2 * sin(radians((-3 * abs))) * (x / 2)}')

print(f'{A}, {B}, {V}, {G}, {D}, {E}, {ZH}, {Z}, {I}, {K}, {L}, {M}, {N}, {O}')
