def find_min(numbers):
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num


numbers = [3, 1, 4, 1, 5]
resul = find_min(numbers)
print(resul)
