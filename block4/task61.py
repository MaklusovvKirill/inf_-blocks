
number = int(input("Введите число: "))


def is_palidrome(n):

    s = str(n)

    return s == s[::-1]


if is_palidrome(number):
    print(f"Число {number} является палиндромом.")
else:
    print(f"Число {number} не является палиндромом.")
