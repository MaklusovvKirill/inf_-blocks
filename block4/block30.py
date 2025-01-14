number = int(input("Введите трехзначное число: "))


def analyze_three_digit_number(num):
    if 100 <= num <= 999:
        digits = [int(d) for d in str(num)]
        a = sum(digits)
        b = digits[0] * digits[1] * digits[2]

        odin = 10 <= a <= 99

        dva = 100 <= b <= 999

        tri = a > b

        chetire = a % 5 == 0

        pyat = (a != 0 and num % a == 0)

        return {
            "Сумма (a) двузначное": odin,
            "Произведение (b) трехзначное": tri,
            "a больше произведения": dva,
            "Сумма кратна 5": chetire,
            "Сумма кратна a": pyat
        }
    else:
        return "Введите трехзначное число."


results = analyze_three_digit_number(number)
print(results)
