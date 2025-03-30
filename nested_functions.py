def calculator():
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /):")

    def addition(number_1, number_2):
        total = number_1 + number_2
        return total

    def subtraction(number_1, number_2):
        total = number_1 - number_2
        return total

    def multiplication(number_1, number_2):
        total = number_1 * number_2
        return total

    def division(number_1, number_2):
        total = number_1 / number_2
        return total

    if operation == "+":
        result = addition(number_1, number_2)
    elif operation == "-":
        result = subtraction(number_1, number_2)
    elif operation == "*":
        result = multiplication(number_1, number_2)
    elif operation == "/":
        result = division(number_1, number_2)
    else:
        result = print("Введиьте корректный оператор (+, -, *, /)")

    print(f"Результат: {result}")
    return result


calculator()
