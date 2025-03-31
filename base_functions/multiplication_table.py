def create_default_list_of_numbers():
    numbers_table_list = []
    i = 0
    while i < 10:
        i += 1
        numbers_table_list.append(i)
    return numbers_table_list


def create_another_list_of_numbers(create_list_of_numbers):
    print(create_list_of_numbers)
    i = 0
    j = 1
    while i < 10:
        i += 1
        default_list = create_list_of_numbers.copy()
        while j < 10:
            j += 1
            multiplied_list = [x * j for x in default_list]
            print(multiplied_list)


create_another_list_of_numbers(create_default_list_of_numbers())
