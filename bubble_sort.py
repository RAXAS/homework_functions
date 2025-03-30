user_list = list(map(int, input("Введите цифры через запятую: ").split(',')))
print(f"Список до сортировки: {user_list}")
n = len(user_list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if user_list[j] > user_list[j + 1]:
            user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
print(f"Список после сортировки: {user_list}")
