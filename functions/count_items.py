def count_items(*args):
    total = len(args)
    return total


result = count_items(4, 6, 8, 9, 5, 2, 5)
print(f"Количество переданных элементов: {result}")
