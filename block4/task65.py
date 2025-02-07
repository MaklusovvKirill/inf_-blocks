n = int(input("Введите год: "))


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if is_leap_year(n):
    print("Год является високосным")
else:
    print("Год не является високосным")
