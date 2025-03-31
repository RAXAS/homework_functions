def count_vowels(string):
    total = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter in vowels:
            total += 1
    return total


string = "Hello World"
result = count_vowels(string)
print(f'Количество гласных в строке "{string}": {result}')
