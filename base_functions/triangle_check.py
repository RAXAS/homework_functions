def check_triangle(a, b, c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        result = print("Треугольник не существует")
    elif a == b == c:
        result = print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        result = print("Треугольник равнобедренный")
    elif a != b and a != c and b != c:
        result = print("Треугольник разносторонний")
    else:
        result = print("Что-то не так, попробуйте ещё раз")

    return result


a = int(input("Введите первую длину треугольника: "))
b = int(input("Введите вторую длину треугольника: "))
c = int(input("Введите третью длину треугольника: "))
check_triangle(a, b, c)
