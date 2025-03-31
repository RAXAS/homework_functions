def print_diamond(rows):
    for i in range(1, rows + 1):
        total = i * "*"
        print(total)
    for i in range(1, rows + 1):
        count = rows - i
        total = count * "*"
        print(total)


rows = 4
print_diamond(rows)
