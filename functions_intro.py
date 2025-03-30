def greet_user(name):
    return print(f"Привет, {name}! Добро пожаловать в мир Python!")


def calculate_sum(a, b):
    result = a + b
    return print(f"Сумма чисел: {result}")


name = input("Введите ваше имя: ")
greet_user(name)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
calculate_sum(a, b)
