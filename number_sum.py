def numbers_from_one_to_n(n):
    count = 0
    numbers_list = []
    total = 0

    while n != count:
        count += 1
        numbers_list.append(count)
    print(f"Числа: {numbers_list}")

    for i in numbers_list:
        total += i
    print(f"Сумма чисел: {total}")


n = int(input("Введите число: "))
numbers_from_one_to_n(n)
