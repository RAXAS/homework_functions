def find_max(a, b):
    if a > b:
        return a
    else:
        return b


number_1 = 10
number_2 = 20
result = find_max(number_1, number_2)
print(f"Максимальное из чисел {number_1} и {number_2}: {result}")
