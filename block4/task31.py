number = int(input("Введите трехзначное число: "))

def all_digits_same(three_digit_number):
    hundreds = three_digit_number // 100
    tens = (three_digit_number // 10) % 10
    units = three_digit_number % 10

    return hundreds == tens and tens == units


result = all_digits_same(number)
print(result)
