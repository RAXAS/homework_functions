def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return "положительное и чётное"
        else:
            return "положительное и нечётное"
    else:
        return "отрицательное"


number = 8
result = check_number(number)
print(f"Число {number} {result}")
