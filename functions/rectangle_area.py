def rectangle_area(length, width):
    rectangle_area = length * width
    return rectangle_area


length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
result = rectangle_area(length, width)
print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {result}.")
