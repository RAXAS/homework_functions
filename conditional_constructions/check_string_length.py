def check_string_length(string, length):
    len_string = len(string)
    if len_string > length:
        return "Длина строки достаточная"
    else:
        return "Строка слишком короткая"


string = "Hello!"
length = 10
result = check_string_length(string, length)
print(result)
