
a = int(input("Введите цифру a (0-9): "))
b = int(input("Введите цифру b (0-9): "))


num1 = 20 + a
num2 = b

result = num1 - num2


tens = result // 10
units = result % 10

print(f"Цифры числа-разности: {tens} и {units}")
