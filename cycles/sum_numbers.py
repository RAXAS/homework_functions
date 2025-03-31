def sum_numbers(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


number = 8
result = sum_numbers(number)
print(f"Сумма чисел от 1 до {number}: {result}")
