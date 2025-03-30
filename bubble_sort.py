user_list = [9, 5, 4, 2, 6, 3]
n = len(user_list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if user_list[j] > user_list[j + 1]:
            user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
print(user_list)
