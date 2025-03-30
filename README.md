# Практические задачи по разделу 3.0 "Функции, Циклы и Управляющие конструкции"

Проект нужен, чтобы лучше углубиться в функции, циклы и конструкции Python. Каждая страница это своя собственная решённая задача, не зависящая от других

## Информация о программах

### age_message.py
При запуске запрашивает год рождения, высчитывает количество лет и выдаёт сообщение исходя из колличества лет: 
1. 0 - 18 лет - Вы еще молоды, учеба — ваш путь!
2. 18 - 65 Отличный возраст для карьерного роста!
3. 65 и больше - Пора наслаждаться заслуженным отдыхом!

Так же, обрабатывает ошибки при вводе года меньше 1900 и больше 2025 

### bubble_sort.py
Просит на ввод цифры через запятую, например "5, 3, 1, 8"

Выводит:

Список до сортировки: [5, 3, 1, 8]

Список после сортировки: [1, 3, 5, 8]

### functions_intro.py
Запрашивает имя, которое выведет. И два числа, которые сложит. 

Например: 

Привет, Дима! Добро пожаловать в мир Python!

Введите первое число: 5

Введите второе число: 3

Сумма чисел: 8

### multiplication_table.py
При запуске выводит таблицу умножения

### nested_functions.py
Калькулятор, который запрашивает два числа и действие, которое нужно с ними провести, например:

Введите первое число: 3

Введите второе число: 7

Введите операцию (+, -, *, /):*

Результат: 21

### number_sum.py
Запрашивает число n, при вводе которого отправляет список от 1 до n и сумму числел от 1 до n. Например:

Введите число: 7

Числа: [1, 2, 3, 4, 5, 6, 7]

Сумма чисел: 28

### triangle_check.py
Запрашивает 3 числа - стороны треугольника. Вычисляет, это треугольник равносторонний, равнобедренный или разносторонний. А так же есть проверка, если две стороны в сумме больше третьей, то отправит ошибку. Например:

Введите первую длину треугольника: 4

Введите вторую длину треугольника: 6

Введите третью длину треугольника: 8

Треугольник разносторонний

## Запуск

1. Скачать проект
2. Открыть проект в PyCharm
3. Запустить нужный файл, например: python age_message.py


```bash
git clone https://github.com/RAXAS/homework_functions.git

python age_message.py

python bubble_sort.py

python functions_intro.py

python multiplication_table.py

python nested_functions.py

python number_sum.py

python triangle_check.py
