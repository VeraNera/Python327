# name = "Vera"
# print("hello,", name)
# print('hello,', name)
# age = 35
# print(age)
# a = 5
# print(a)
# print(id(a))
# print(type(a))
# a = 'hello'
# print(a)
# print(id(a))
# print(type(a))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 'hello', 5, 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# print('строка \nсимволов')
# print("строка")

# s1 = "hello"
# s2 = "world__"
# s3 = s1 + " " + s2
# print(s3 * 3)

# print(4545465465464646464646464645)
# print(4.545465465464646464646464645)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 4)
# print(6 // 4)
# print(6 ** 2)
# print(6 % 4)

# a = 5
# b = 7
# c = 3
# p = a + b + c
# print("сумма:" + p)
# print("произведение:" + a * b * c)
# print("средне-арифметическое:" + (a * b * c) / 3)


# num = 4321
# a = num % 10
# print("a:", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print(num)

# num1 = 4321
# print(num1)
# res = num1 % 10 * 1000
# num1 = num1 // 10
# res += num1 % 10 * 100
# num1 = num1 // 10
# res += num1 % 10 * 10
# num1 = num1 // 10
# res += num1 % 10
# print(res)

# num = 10
# num += 5
# print(num)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a

# num1 = "2"
# num2 = 3
# print(type(num1))
# print(type(num2))
# # res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(float(3.8945))
# print(int(3.8945))

# a = 3.8945
# a = round(a, 1)
# print(a)
# print(type(a))
# print(round(3.8945, 2))  #округляет

# num1 = "5.2"
# num2 = 10
# print(type(num1))
# print(type(num2))
# res = float(num1) + num2
# print(res)

# name = "Вера"
# age = 28
#
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print()
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" ")
# print("Продолжение строки.")

# name = input("ведите имя: ")
# print("Hello,", name, "!", sep="")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# # res = int(num) ** int(power)
# res = num ** power
# print(res)

# num1 = input("Введите число: ")
# num2 = input("Введите число: ")
# num3 = input("Введите число: ")
# num4 = input("Введите число: ")
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = round(sum1 / sum2,2)
# print(res)

# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)
#
# print(type(b1))

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# a = None
# print(a)
# print(a is None)  # True
# a = 3
# print(a)

# print(5 > 2)  # True
# print(5 < 2)  # False
# print("привет" > "Привет")  # True

# print(2 < 4 < 9)  # True
# print(2 < 4 > 9)  # False
# print(2 * 5 > 7 >= 4 + 3)  # True && True
# print(3 * 3 <= 7 >= 7)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c) # 10 5 False

# && - and
# || - or
# ! - not

# print(5 - 3 == 2 and 1 + 3 == 4)  # True
# print(5 - 3 == 2 or 1 + 3 == 4)  # True

# print(not 9 - 5)  # false преобразование в противоположное значение
# print(not 9 - 9)  # True

# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)  # функция, принт в теле функции
#
# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)  # принт не в теле функции

# age = int(input("введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 16
# b = 5
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# else:
#     print("b == a")  # работает только с одним if сверху


# a = 16
# b = 5
# if a > b:
#     print("a > b")
# elif b > a:  # если два if, то пишется через elif. if / else используется только один раз
#     print("b > a")
# else:
#     print("b == a")

# a = input("Введите сторону треугольника: ")
# b = input("Введите сторону треугольника: ")
# c = input("Введите сторону треугольника: ")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("треугольник разносторонний")

# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Не существует")

# month = int(input("Введите месяц цифрой: "))
# if 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# elif month == 12 or month == 1 or month == 2:
#     print("Зима")
# else:
#     print("Ошибка ввода")

# 20 июня____________________________

# n = int(input("Введите количество ворон (0-9): "))
# if 0 <= n <= 9:
#     print("На ветке", end=' ')
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#         print('ошибка ввода')

# password = 'admin'
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print("Модератор")
#     case_:
#         print("Пароль не верен")

# day = 'понедельник'
# time = 13
#
# match day:
#     case 'Понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("выходной день")
#     case _:
#         print("Такого дня не существует или не рабочее время")

# Тернарное выражение

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 30
# minim = a if a < b else b
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 30, 10
# minim = a if a < b else b
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 30, 40
# minim = a if a < b else b
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 2, 10
# print("Делить на 0 нельзя"if b == 0 else a /b)
# print(a / b)

# Синтаксические ошибки в папке 4


# try:  # попробовать
#     n = int(input("Ведите целое число: "))
#     print(n * 2)
# except ValueError:  № исключение
#     print("Что то пошло не так")
# except ZeroDivisionError:
#       print("нельзя делить на 0")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("нельзя вводить строки. нельзя делить на 0")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. вы ввели числа", n, "и", m)
# finally:  # выводится в любом случае
#     print("конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

#  итерация -  один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     print(i, end=" ")
#     i += 2  # не четные

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1  # четные


#  1 способ
# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end=" ")
#     i += 1

# 2 способ
# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
# #     n -= 1
#     print("*" * n)

# a = int(input("Укажите начало диапазона: "))
# b = int(input("Укажите конец диапазона: "))
# res = 0
# while a <= b:  # 1 3 5
#     if a % 2:  # a % 2 == 1  # a % 2 !=0
#         res += a  # res = res + a
#         print(a)
#     a += 1
# print("Сумма нечетных чисел:", res)

# n = input("Введите целое число: ")

# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# i = 0
# while i < 10:
#     print(i, end="")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end="")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# res = 1
# while True:
#     n = int(input("введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# 22 uny

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("Внутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 3:  # отвечает за количество строк
#     j = 1
#     while j <= 6:  # отвечает за количество столбцов
#         print("^", end="\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:  # отвечает за количество строк
#     j = 1
#     while j <= 16:         # отвечает за количество столбцов
#         if j % 2:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# for i in "Hello":
#     print(i)

# for color in 'red', 'blue', 'green':
#     print(color)

# for i in range(5):
#     print(i)


# for i in range(5, 100, 10):  # (start, stop, step)
#     print(i, end=" ")
#
# print()
#
# i = 5
# while i < 100:
#     print(i, end=" ")
#     i += 10


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

#  1 вариант
# for i in range(11, 100, 11):
#     print(i, end=" ")

# 2 вариант
# for i in range(11, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Done!")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# 1 способ
# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите длину прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         print("*", end=" ")
#     print()
# 2 способ
# a = 16
# b = 4
# for i in range(b):
#     for j in range(a):
#         if i == 0 or j == 0 or i == b - 1 or j == a - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# a = [letter for letter in "Hello"]
# print(a)

# num = [i for i in range(20)]
# print(num)

# num = [i for i in range(20) if i % 2 == 0]
# print(num)

# Список (list)
# nums = [8, 3, 2, 4, "Hello", 1, 15, 2.5]
# print(type(nums))  # <class 'list'> тип данных
# print(nums)
# print(nums[0])
# print(nums[5])
# print(nums[-2])
# nums[3] = 256
# nums[0] += 108
# print(nums)

# s = []
# print(s)
# print(type(s))
# b = list("Hello")
# print(b)
# print(type(b))

# n = list(range(2, 10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)

# n =5
# a = [i for i in range(1, n + 1)]
# print(a)

# a = [i *3 for i in 'list']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)

# a = [0] * int(input('Количество элементов в списке: '))
# print(a)
# for i in range(len(a)):
#     a[i] = input("->")
# print(a)

# a =[int(input("->")) for i in range(int(input('n: ')))]
# print(a)

# a = ['один', 'два', 'три', 'четыре', 'пять']
# for i in range(len(a)):  # 0 1 2 3 4 - индексы
#     print(a[i], end=" ")
# print()
# for el in a:  # один два три четыре пять
#     print(el, end=" ")

# a = [int(input("->")) for i in range(int(input('n=')))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print('Сумма отрицательных элементов равна:', s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print('Количество четных элементов:', k)
# print('Сумма нечетных элементов:', s)

# a = [int(input("->")) for i in range(int(input('n: ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")


# модули из интерпритатора---------------------------------------------------------------

# import math
# num_1 = math.sqrt(4)
# num_2 = math.ceil(3.2)
# num_3 = math.floor(3.8)
# num_4 = math.pi
# print(num_1)
# print(num_2)
# print(num_3)
# print(num_4)
#
#
# import math as m
# num_2 = m.ceil(3.2)
# num_3 = m.floor(3.8)
# print(num_2)
# print(num_3)

# from math import ceil, floor
# num_2 = ceil(3.2)
# num_3 = floor(3.8)
# print(num_2)
# print(num_3)

# from math import *
# num_2 = ceil(3.2)
# num_3 = floor(3.8)
# print(num_2)
# print(num_3)


# import time

# sec = time.time()
# print(sec)
#
# local = time.ctime(168788366)
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)

# import time

# import locale
# locale.setlocale(locale.LC_ALL, "")

# print(time.strftime("Сегодня %B %d, %Y"))
# print(time.strtime("%d/%m/%Y, %H:%M:%S"))

# print("программа запустилась......")
# time.sleep(5)
# print("Программа завершена")


# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("программа запустилась......", finish - start, "секунд")


# Срезы: список{start:stop:stop]---------------------------------------------------------------
# s = [5, 8, 2, 5, 8]
# print(s[1:3])  # вытащить число с помощью индекса
# print(s[:: -1])  # развернет список
# print(s[0:-1:2])  # вывод каждый 2 элемент от 0
# print(s[4:0:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1])
# print(s[6:])
# print(s[3:4])
# print(s[-3:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]  # добавление элементов
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []  # удаление элементов
# print(s)
# del s[:]  # удаление элементов текущих
# print(s)

# s = [1, 2, 3, 4, 5, 6, 7]
# s[6] = 8  # перезапись элемента
# print(s)

# методы списков
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([8, 9, 10])  # добавляет несколько элементов
# print(s)
# s.extend("add")
# print(s)
# s.insert(5, 100)  # вставляет объект не удаляя, а сдвигая элементы первый параметр -это индекс, второй - добавляемое значение
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0,x)
# print(s)

# s = []
# n = int(input("введите число кратное 3: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "Не делится без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])  # объединяет списки [1, 11, 2, 22, 3, 33]
#     c.append(b[i])
#
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# print(c)


# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# s.remove(0)  # удаляет первый найденный элемент по заданному значению
# print(s)
# last = s.pop()  # удалил последний элемент из списка
# print(last)
# print(s)
#
# last = s.pop(-3)  # удалил  элемент из списка по заданному индексу
# print(last)
# print(s)
#
# s.clear()  # очищает список
# print(s)

# a = [int(input("->")) for i in range(int(input('n= ')))]
# print(a)
# print("Введите индексЖ ")
# k = int(input("k = "))
# a.pop(k)
# print(a)


# s = [4, 0, 0, 5, 6, 8, 3, 4]
# print(s)
# num = s.count(0)  # считает кол-во заданных элементов в списке
# print(num)
#
# ind = s.index(3)  # возвращает индекс первого найденного элемента по его значению
#
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))  # два одинаковых списка, но в разных ячейках памяти
# print("b =", b, id(b))
# a.append(20)
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(30)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 2, 3]
# a.reverse()  # перестраивает элементы списков в обратном порядке
# print(a)


# s = [9, 7, 6, 4, 0, 2, 3]
# s.sort()  # сортировка по возрастанию
# print(s)
#
# s = [9, 7, 6, 4, 0, 2, 3]
# s.sort(reverse=True)  # сортировка по убыванию
# print(s)

# s2 = ["Алексей", "Александр", "Виталий", "Юрий", "Сергей"]
# s2.sort(key=len, reverse=True)
# print(s2)


# s = [4, 6, 9, 7, 1, 8, 2]
# s.sort()  # ничего не возвращает через принт
# print(s)
#
# s2 = [4, 6, 9, 7, 1, 8, 2]
# s3 = sorted(s2)  # возвращает
# print(s3)
# print(s2)


# генерация случайных данных---------------------------------------------------------------

# import random

# print(random())
# print(randint(0, 9))  # конечное значение включает (включая 9)
# print(randrange(9))  # не включает конечное значение (не включая 9)
# print(randrange(2, 9, 2))  # от 2 до 9 только четные значения не включая конечный диапазон 9
#
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))


# city = ["Москва", "Воронеж", "Псков", "Казань"]
# # print(choice(city))
# print(choices(city, k=3))
#
# s = [55,66,34,87,9,11,23,45,6,8,9,4,3,]
# print(choices(s,k=5))


# from random import randint
#
# a = [randint(50, 100) for i in range(10)]
# print(a)


# lst = [6, 4, 1, 7, 9, 5]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# lst = [19, 71, 22, 27, 52, 50, 88, 57, 10, 19]
# print(lst)
# m = max(lst)
# print("Max: ",m)
# lst.remove(m)
# print(lst)
# lst.insert(0, m)
# print(lst)


# from random import randint

# a = [randint(1,100) for i in range(10)]
# print(a)
# minim = min(a)  # ищет минимальное значение и удаляет все значения перед ним
# print("Min:", minim)
# ind = a.index(minim)
# print(ind)
# del a[:ind]
# print(a)

# x = list('kjdfoi4i4i5j')
# print(x)
#
# print('a' in x)
# print('f' in x)

# lst = []
# if not lst:  #  len(lst) == 0:
#     print("Список пустой")
#
# print(bool(lst))  # false

# from random import randint

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:  # проверка наличия значений в списки, которые повторяются
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])  # добавление в список значений из двух списков все, что не повторяется
#
# print("Третий список: ", c)

# for i in range(n1):
#     if a[i] in b and a[i] not in c:  # проверяем еть ли элемент во втором списке и есть ли в третьем
#         c.append(a[i])
#
# c = (min(a), min(b), max(a), max(b))
# print("Третий список: ", c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print()
# print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t\t')
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)


# from random import randint
# w,h = 5, 4
# matrix = [[randint(1,30) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()

# from random import randint
#
# a, b = 3, 4
# s = 0
# matrix = [[randint(-20,10) for x in range(a)] for y in range(b)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end='\t\t')
#     print()
# print(s)

# функции
# print()
#
#
# def hello(name, word):  # аргументы
#     print("Hello", name, "Say", word)  # функция отделяется от кода двумя пустыми строками до функции и после нее
#
#
# hello("Вера", "hi")  # параметры
# hello("hello", "Ivan")

# def get_sum(a, b):
#     print(a + b)
#
# n = 2
# m = 3
# get_sum(n, m)
# c = 5
# d = 6
# get_sum(c, d)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a,end="")  # 0123456789 = 'a'
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     return a + b
#
#
# n = 2
# m = 3
# res = get_sum(n, m)
# print(res ** 2)


# def add(x, y):
#     if x > y:
#         return x - y
#     return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print("Результат: ", m)

# def cube(a):
#     return a * a * a
#
# for i in range(1, 11):  # указывается от какого числа до какого числа
#     print(i, 'в кубе =', cube(i))


# def change(lst):
#     a = lst.pop()  # получили последний элемент
#     b = lst.pop(0)  # первый элемент
#     lst.append(b)
#     lst.insert(0, a)
#     return lst

# lst[0], lst[-1] = lst[-1], lst[0]  # поменять местами первый элемент и последний элемент местами
# return lst


# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# a = 5
# b = 12
# print(func(10, 5))
# print(func(10, 10))
# if func(a, b):
#     print("первое число больше второго")
# else:
#     print("Нет")


# def check_pass(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Ведите пароль: ")
# if check_pass(p):
#     print("Это надежный пароль")
# else:
#     print("Ненадежный пароль")


# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1,d=2, b=5))


# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()
# set_param(s="?")


# def digits_sum(n, even=True):  # 9874023
#     s = 0
#     while n >0:
#         cur_digit = n % 10  # 3
#         if even and cur_digit % 2 == 0:  # проверка на четное число без even
#             s += cur_digit  # s = 2
#         elif not even and cur_digit % 2 != 0:  # нечетные числа
#             s += cur_digit
#         n //= 10  # деление числа на цело 9удаляется последняя цифра
#     return s
##
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name,age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")  # лишний аргумент - имя, т.к. имя уже задано выше


# a = 5
# print(a, id(a))
# a = 6
# print(a, id(a))
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])
# print(lst1, id(lst1))

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
# print(a, id(a))
# print(b, id(b))

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# print(a, id(a))
# print(b, id(b))

# Списки изменяемые тип данных, строковые значения неизменяемые типы данных, при ссылке на ячейку памяти

# изменяемые типы данных - list, set
# неизменяемый тип данных - int, str, float, bool, tuple

# st = "Hello"
# print(st[-1])
# st = list(st)  # преобразуем в другой тип данных для изменения буквы/числа
# st[-1] = 'q'
# print(st)


#  кортежи (tuple)----------------------------------------------------------------------------

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a =
# a = tuple((4, 5, 6, 7))  # принимает один элемент
# print(a)
# print(type(a))
# print(a[-1])
# print(a[1:3])

# s = tuple([input("=>") for i in range(5)])
# print(s)
# from random import randint
# s = tuple(randint(0, 10) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))  # возведение в степень через кортеж
# print(s)


# t1 = tuple("hello")  # сложение кортежей
# t2 = tuple("world")
# t3 = t1 + t2
# # print(t3 * 2)  # умножение работает
# print(t3)
# print(t3.count('l'))  # посчитали сколько таких символов
# ch = 'o'
# if ch in t3:
#     print(t3.index(ch))
# else:
#     print('Такого символа нет')
#
# print(t3.index('l'))  # какой индекс у символа
# for i in t3:
#     print(i * 2,end=" ")


# def slicer(tpl, el):  # el = 8
#     if el in tpl:
#         if tpl.count(el) > 1:  # посчитали количество 8
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)  # индекс второй восьмерки
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 8, 5, 1, 2, 9), 8))


# from random import randint
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl_1 = ran(0, 5)
# tpl_2 = ran(-5, 0)
# print(tpl_1)
# print(tpl_2)
# tpl_3 = tpl_1 + tpl_2
# print(tpl_3)
# print("0 =", tpl_3.count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6,], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"  # заменили слово в кортеже по индексу
# t[4].append("hi")  # добавили слово в конец списка
# print(t, id(t))
# del t[4][0]  # удаление элементов
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # n, year, married = user
# n, year, married  = get_user()  # сразу распаковываем кортеж
# print(n, year, married)


# tpl = (10,20,30)
# del tpl  # из кортежа не можем удалять, удаляется ссылка на кортеж

# tpl = (10,20,30)
# lst = list(tpl)  # преобразовали в список, измнили и обратно в кортеж
# print(lst)
# lst.append(50)
# print(lst)


# countries  = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 80.2, (("Париж", 3.326), ("Марсель", 1.718))),
# )
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ". Население: ", country_population, cities, sep="" )
#     for city in cities:
#         city_name, city_population = city
#         print("\nГород: ",city_name, ". Население: ", city_population, sep="")


# Множество (set) неупорядочный коллекционный тип данных
# s = {"banana", "apple", "orange"}  # хранит уникальные данные, которые не повторяются
# print(s)
# print(type(s))
# for i in s:
#     print(i)

# a = set()
# print(a)
# print(type(a))

# s = {i * i  for i in range(10)}  # сгенерировали список от 0 до 9
# print(s)
# print(64 in s)  # находится число 64 или нет в списке

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' in i}
# # a = ["A" + i[1:] if i[0] == 'a' else 'B' +i[1:] for i in s]
# a = ["A" + i[1:] if i[0] == 'a' else 'B' +i[1:] for i in s if i[1] == 'c']
# print(a)
#
# for i in s:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#     else:
#         print('B' +i[1:])


# a = {"Tom", "Bob", "Alice"}
# a.add("Sam")
# print(a)
# # a.remove("Tom")
# # a.remove("Ann")  # KeyError
# # print(a.pop())  # удаляет первый элемент -случайный
# a.clear()  # удалил текущий
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)  # объединил, но повторы не сохраняет
# # c = a | b  # такая же информация как и предыдущая
# # c = a & b  # пересекающиеся элементы
# c = a - b
# c = a ^ b
#
# # a |= b  # пересохранили в переменную
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7  # сложение через оператор
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s = frozenset([1, 2, 3, 4, 5])  # замороженный сет, неизменяемый
# print(s)

#  Словари (dict)---------------------------------------------------------------------------

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 3: 0}
# print(type(d))
# print(lst[0])
# print(d['one'])
# print(lst[2])
# print(d[3])

# d = {}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))


# users = [('a', 'b'), ['c', 'd'], ['e', 'f']]
# print(users)
# d_users = dict(users)
# print(d_users)
# lst = list(d_users)
# print(lst)

# d = {i: i for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20
# print(d)

# d = {0: 'text', 'one': 1, (1, 2.3): 'кортеж', 'список': [2, 3, 7, 6]}
# print(d)
# print(d[(1, 2.3)])
# print(d['список'][2])
# print('one' in d)
# print('text' in d)
# del d[0]
# print(d)

# d = {'one': 1, "two": 2, 'three': 3}

# for i in d:  # проходимся по словарю
#     print(i, d[i])
#
# if key in d:
#     del d[key]
# print(d)


# d = {'one': 1, "two": 2, 'three': 3}
# key = 'four'
# try:
#     del d[key]
# except KeyError:
#     print('Такого элемента нет')
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
#
# res = 1
# for key in d:
#     res *= d[key]
# print(res)


# d = dict()  # {} тоже самое = пустой словарь
# d[1] = input("-> ")
# d[2] = input("-> ")  # добавляется словарь
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# print(len(d))
# print(min(d))
# print(max(d))

# goods = {
#     '1': ['Core-i3-4300', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.",  sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input("Количество: "))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.",  sep="")


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений одновременно кортеж
# # for i, j in d.items():
# #     print(i, j)
#
# print(list(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy
# print("D =", d)
# print("D2 =")
#
# d2['b'] = 5
# d['e'] = 7


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.update({'r': 7, 't': 9})  # добавление  обновление словаря в словарь
# d.update([('s', 9), ('q', 8)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y  # помещение двух словарей в третий
# print(z)

# d = {'a': 1, 'b': 3, 'c': 4}
# print(d)
# # d.clear()  # очистить словарь полностью
# # item = d.pop('b')  # удаляет ключ и значение по ключу, но возвращает именно значение
# item = d.popitem()  # удаляет последнее значение и ключ и возвращает кортеж удаляемых элементов
# print(item)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# # new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five',
#     }
# }
# print(a)  # как можно сделать через методы? до.задача
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four',-20]
# s = dict()
# n = None
#
# for i in a:  # перебор списка
#     if type(i) == str:  # преобразование в строковое значение
#         s[i] = []  # создали ключи из списка
#         n = i  # n = 'one'
#     else:
#         s[n].append(i)  # s['one'] = [1, 2, 3]
#
#
# print(s)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# s = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(s)


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# c = [4.0, 8.5, 6.3]
# d = ['a', 'b']
# b = list(zip(a, c, d))
# print(b)

# dict_one= {'name': 'Igor', 'last_name': 'Doe', 'job': 'consultant'}
# dict_two= {'name': 'Ira', 'last_name': 'Smith', 'job': 'manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# two = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'four')]
# a, b = zip(*two)  # распаковка кортежа с помощью zip
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.7, 'onion': 0.55}
# print({**one, **two})


# s = ['red', 'blue', 'green']
# # j = 1
# for j, i in enumerate(s, 1):
#     print(j, ') ', i, sep="")
#     # j += 1
#

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 4, 6))


# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(3, 4, 6))


# def ch(*args):
#     average = sum(args) / len(args)
#     print('Среденее арифметическое: ', average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
#
# def func(a, *args):
#     return a, args
#
# print(func(5))
# print(func(5, 4, 5, 6, 7, 8, 1))


# def print_scores(student, *scores):
#     print("Student:", student, end=": ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonatan", 100, 95, 88, 92)
# print_scores("Rick", 96, 28)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#
# info(name="Irina", famyli="Georg", age="22", phone='13256478',)
# info(name="Inna", famyli="Leo", age="25",email="mamamia@gmail.com", phone='13256478', country="Russia")


# def func(a, *args, d=1, **kwargs):
#     return a, args, kwargs, d
#
#
# print(func(5, 1, 7, 9, 8, b=2, c=3, d=1))


# name = 'Tom'  # глобальная переменная
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jhon"  # локальная переменная
#     print("hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 6
#
#
# def func(a):
#     x = 2
#
#     def inner():
#         x = 4
#         return a + x
#
#     return inner()
#
#
#
# print(func(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# def outer(who):
#     who = "Alex"
#
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("world!")


# def fun1():
#     a = 6  # выполняется второй
#
#     def fun2(b):
#         a = 4  # выполняется пятым
#         print("Сумма: ", a + b)
#
#     print("a =", a)  # выполняется третьим
#     fun2(4)  # выполняется четвертым
#
#
# fun1()  # выполняется первой


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal  x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# простой способ решения задачи из ДЗ, через локальную переменную
# def outer(a, b, c):
#     def inner(x, y):
#         return x * y
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# Замыкание-------------------------------------------------------------------------------

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(20))
#
# print(outer(4)(6))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()


# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "David": 75,
#     "Ella": 64,
#     "Fiona": 35,
#     "Alex": 69
# }
#
#
# def make(lower, upper):
#     def inner(exam):
#         return{k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# bal_A = make(80, 100)
# bal_B = make(70, 80)
# bal_C = make(50, 70)
# bal_D = make(0, 50)
# print(bal_A(students))
# print(bal_B(students))
# print(bal_C(students))
# print(bal_D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())  # summa
# print(obj1.sub())  # разность
# print(obj1.mul())  # произведение


# анонимны функции (lambda выражения)--------------------------------------------------------


# def summa(x=5, y=7):
#     return x + y
#
#
# print(summa(1, 2))
#
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 7, 8, 9))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))  # первый способ
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(42)
# print(f1(1))  # второй способ
#
#
# outer2 = lambda  n: lambda  x: x + n
#
#
# f2 = outer2(42)
# print(f2(1))  # трети1 способ
#
# print((lambda n: lambda x: x + n)(42)(1))  # четвертый способ

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'c': 10, 'a': 15, 'b': 4}
# q = list(d.items())
# print(q)
# q.sort(key=lambda i: i[1], reverse=True)
# print(q)
# d1 = dict(q)
# print(d1)

# Задача

# players = [
#     {'name': 'Алла', 'last name': 'Иванова', 'rating': 9},
#     {'name': 'Игорь', 'last name': 'Егоров','rating': 10},
#     {'name': 'Егор', 'last name': 'Лебедев','rating': 4},
#     {'name': 'Дмитрий', 'last name': 'Силаев','rating': 6},
# ]
#
# res = sorted(players, key=lambda  item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y),(lambda x, y: x / y)]
# b = a[3](12, 5)  # обратились по индексу списка в круглых скобках параметры функии x y
# print(b)


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[2]()


# map(func, iter), filter(func, iter)-------------------------------------------------------

# def mult(t):
#     return t * 2


# lst =[2, 8, 12, 5, 10]

# a = list(map(mult, lst))
# a = list(map(lambda t: t * 2, [2, 8, 12, 5, 10]))
# print(a)


# t = (2.88, -3.5, 100.65)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t3 = tuple(map(int, t))
# print(t3)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 =[1, 2, 3]  # x
# l2 = [4, 5, 6]  # y
#
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)


# filter(func, iter)------------------------------------------------------------

# t = ('adcd', 'abc', 'sere', 'dass', 'edf')
# t2 = tuple(filter(lambda s: len(s) == 3, t))  # функция возвращает значение, элемент попал под условие которое указано
# print(t2)


# b = [66, 98, 68, 59, 76, 88, 74, 91, 83, 65]
# res = list(filter(lambda s: (s > 75) and s < 80, b))
# print(res)


# декоратор------------------------------------------------------------------
# def hello():
#     return 'hello "Hello"'
#
#
# def super_func(func):
#     print('hello "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello "hello"'
#
#
# print(id(hello))
# test = hello
# print(id(test))
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello 'func_test")
#
#
# test = my_decorator(func_test)
# test()

#
# def my_decorator(func):  # декорирующая функция, чем декорируем
#     def wrap():
#         print('*' * 20)
#         func()
#         print('=' * 20)
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello 'func_test")
#
#
# def hello():
#     return 'Hello "hello"'
#
#
# func_test()
# print(hello())


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "test"
#
#
# print(hello())


# def cnt(fn):
#     c = 0
#
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print("Вызов функции:", c)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_dekorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_dekorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Селезнева")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
# #

# def decor(args1):
#     def args_dac(fn):
#         def wrap(x, y):
#             print(args1, x, "и",  y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dac
#
#
# @decor("Сумма:")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("разность:")
# def sub(a, b):
#     print(a - b)
#
#
# summa(2, 5)
# sub(5, 2)

# def multyplay(arg):  # 3
#     def outer(func):  # return_num
#         def wrap(*args, **kwargs):  # num
#             arg * func(*args, **kwargs)
#
#             return wrap
#     return outer
#
#
# @multyplay(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("неверный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("неверный тип данных")
#
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return outer
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed_fn3(str, str, z=int)
# def typed_fn3(x, y, z="hello"):
#     return(x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "!"))
#
# print(typed_fn2("hello", "world", "!"))
# # print(typed_fn2(6, 4, 2))
#
# print(typed_fn3("hello", "world", z='5'))

# print(int('100', 3))
# print(int('100', 6))
# print(int('100', 2))


# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0x12)
# print(0b10010)
# print(0o22)
# print(0o22 + 0b10010)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print('t' in e)
# print(e[:: -1])

# print("привет")
# print(u"привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
#
# print(r"C:\folder\file.txt\\"[:1])
# print(r"C:\folder\file.txt" + "\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне" + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# print(f"число: {round(10 / 3, 2)}")
# print(f"число: {10 / 3:.2f}")


# x = 10
# y = 5
# # print(f"{x=}, {y=}")
# # print(f"{x=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")  # 10*5/2=25.0


# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')


# s = """Hello
# world!"""   # тройные кавычки сохраняют форматирование (переносы на новую строку)
# s1 = '''Hello
# world!'''
# print(s)
# print(s1)


# def square(n):
#     '''Принимает число n, возвращает квадрат числа n'''
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)  # возвращает документацию(комментарий) к функции, указанные выше


# import math
#
#
# def cylinder(r, h):
#     '''
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     '''
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))  # код символа
# print(ord('A'))



# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# s = "Test string for met"
# arr = [ord(x) for x in s]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое; ", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(1056))


# a = 97
# b = 122
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")
# print(ord('a'))
# print(ord('A'))

# from random import randint
#
# SHORTEST = 8
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         # print(rand_char)
#         res += rand_char
#
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python!"
# print(s.capitalize())  # Hello, world! i am learning python!
# print(s.lower())  # hello, world! i am learning python!
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON!
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON!
# print(s.title())  # Hello, World! I Am Learning Python!

# print(s.count("h", 1, -4))  # кол-во заданных элементов

# print(s.find("Python"))  # возвращает индекс заданного элемента или -1 если элемента нет
# print(s.rfind("h"))  # поиск с конца

# print(s.index("Python1"))  # возвращает индекс заданного элемента или ValueError: если элемента нет
# print(s.rindex("h"))  # поиск с конца

# print(s.startswith("hello"))  # поиск заданной подстроки с начала, возвращает  bool true /false
# print(s.endswith("Python"))  # поиск заданной подстроки с конца, возвращает  bool true /false


# s1 = "I am learning Python. hello, WORLD!"
# s1 = s1[:s1.find('h')] + s1[s1.rfind('h') + 1:]
# print(s1)

# print('abc123'.isalnum())  # состоит ли строка из букв или  цифр
# print('AFVhh'.isalpha())  # состоит ли строка из букв
# print('123'.isdigit())  # состоит ли строка из цифр
# print('adc'.islower())  # проверяет наличие только  букв в нижнем регистре
# print('VFGNN'.isupper())  # проверяет наличие только  букв в верхнем  регистре


# print('py'.center(10, "-"))  # выравнивание по центру
#
# print("   py")
# print("   py".lstrip())  # убирает проблемы слева
# print("py    ".rstrip())  # убирает пробелы справа
# print("   py       ".strip())  # убирает пробелы слева и справа


# print('https://www.python.org'.lstrip('/:pths'))
# print('https://www.python/.org'.lstrip('/:pths'). rstrip("org."))
# print('https://www.python.org/'.strip('/:pthsorg.'))


# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык."
# print(s.replace('Nython', 'Python', 2))

# преобразует итерируемый объект в строку
# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("...".join(["1", "99"]))
#
# print(":".join("Hello"))

# print('Строка разделенная пробелами'.split())  # разбивает строку на список подстрок
# print("www.python.org.ru".split(".", 2))
# print("www.python.org.ru".rsplit(".", 1))


# a = input("-> ").split()  # образовывает сразу в список
# print(a)

# a = input("-> Введите ФИО: ").split()
# print(a)
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')


# Регулярные выражения-----------------------------------------------------------------


import re
#
s = "Я ищу совпадения в 2023 году. [^] И я их найду в 2 счёта. 47_896. hello world"
# reg = r'\d'  # [3-5]
# reg = r'\d+'
# reg = r'\d*'
# reg = r'20*'
# reg = r'\d?'
# reg = r'\w'
reg = r'\s'
# reg = r'\S'
# reg = r'\W'
# reg = r'\D'
# reg = r'\AЯ ищу'
# reg = r'world\Z'


# reg = r'[2023]'
# reg = r'[12][0-9][0-9][0-9]'  # 12 = 1 или 2
# reg = r'[А-ЯЁа-яё]'
# reg = r'[\[^\]]'
# reg = r'[^0-9]'

# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # возвращает первое совпадение с искомым шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.split(reg, s, 5))  # разбивает строку на список по заданному шаблону

# print(re.sub(reg, "!", s))  # поиск и замена

# print(re.findall(reg, s))
# print(ord("ф"))
# print(ord("я"))
# print(ord("ё"))


# import re

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:59. Минуты в диапазоне от 00 до 59. 21-06-15Т01:09."
# reg = '[0-2][0-9]:[0-5][0-9]'
#

# + - от 1 до бесконечности повторений
# *  - от  0  до бесконечности повторений
# ? - от 0 до 1 повторений

# d = "цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?[\d.]+', d))





# def avg(fn):
#     def wrap(*args):
#         a = ", ".join(map(str, args))
#         print(*args)
#         print(args)
#         print("Среднее арифметическое: ", a, "=",  fn(*args) / len(args))
#
#     return wrap
#
# @avg
# def summa(*args):
#     print("Сумма чисел: ", *args, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# 15 августа

# print('Hello')
# print("good")


import re

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('#.*', '', s))
# print(re.sub('-', '.', s))
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', s)))


# a = '12 сентября 2023 года'
# req = r'\d{2,4}'
# print(re.findall(req, a))


# a = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# req = r"\+?7\d{10}"
# print(re.findall(req, a))


# a = "Я ищу совпадения в 2023 году. И я их найд в два счета."
# # reg = r'^\w+\s\w+'
# req = r'\w+\.$'
# print(re.findall(req, a))


# def validate_login(name):
#     return re.findall(r'^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login("Python_master"))
# print(validate_login("#%$jlff"))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w+", text, flags=re.DEBUG))


# b = "Я ищу совпадения в 2023 году. И я их найд в 2 счета."
# req = 'я'
# print(re.findall(req, b, re.IGNORECASE))

#
# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall('one$',text))
# print(re.findall('one$',text, flags=re.MULTILINE))


# # print(re.findall("""[a-z.-]+@[a-z.-]+""", 'test@mail.ru'))
# print(re.findall("""
# [a-z.-]+
# @
# [a-z.-]+
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# req = "(?im)^python"
# print(re.findall(req, text))

# text = "<body>Пример соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # req = r'<img.*?>'
# req = r'<img[^>]*>'
# print(re.findall(req, s))


# d = "Петр, Ольга и Виталий отлично учатся"
# req = "Петр|Ольга|Виталий|Николай"
# print(re.findall(req, d))

# a = "int = 4, float = 4.0, double = 8.0f"
# req = r"\w+\s*=\s*\d+[.\w+]*"
# print(re.findall(req, a))

# # a = '127.0.0.1'
# a = '192.168.255.255'
# # req = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
#
# print(re.findall(req, a))


# a = "Word2016, PS6, AI5"
# req = r'(([a-z]+)(\d+))'
# print(re.findall(req, a, re.I))


# a = "5 + 7*2 - 4"
# req = r'\s*[+*-]\s*'
# print(re.split(req, a))
#
# a1 = "5 + 7*2 - 4"
# req1 = r'\s*([+*-])\s*'
# print(re.split(req1, a1))


# a = "28-08-2021"
# # req = r'\d{2}-\d{2}-\d{4}'
# req = r'(0[1-9]|[12][0-9]|3[01])-(\d{2})-(\d{4})'
# print(re.findall(req, a))


# b = "Я ищу совпадения в 2023 году. И я их найд в 2 счета."
# req = r'(\d+)\s(\D+)'
# print(re.search(req, b).group())
# m = re.search(req, b)
# print(m[1])
# print(m[2])
# print(m[0])

#
# text = """
# Cамара
# Лобня
# Москва
# Торжок
# Уфа
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", repl_find, text))


print("У меня все получилось!!!")