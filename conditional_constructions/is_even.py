def is_even(number):
    if number % 2 == 0:
        return "чётным"
    else:
        return "нечётным"

number = 7
is_even = is_even(number)
print(f"Число {number} является {is_even}")