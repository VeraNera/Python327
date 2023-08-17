from math import pi

print("1-прямоугольник, 2-треугольник, 3-круг")
figure = input("Выберите фигуру: ")
if figure == '1':
    a = 40
    b = 2
    print("Площадь прямоугольника: ", (a * b))
elif figure == '2':
    o = 10
    v = 16
    print("Площадь треугольника: ", 0.5 * o * v)
elif figure == '3':
    r = 2
    print("Площадь круга: ", round(pi * r ** 2, 2))
else:
    print("Ошибка ввода")
