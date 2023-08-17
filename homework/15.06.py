# ДЗ-2

num = int(input("Введите пятизначное число: "))
print("Вы ввели число: ",  num)

# Разбиваем число на цифры
digit1 = num // 10000  # получили первую цифру
digit2 = (num // 1000) % 10
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10
res = digit1 * digit2 * digit3 * digit4 * digit5
res2 = (digit1 + digit2 + digit3 + digit4 + digit5) / 5
print("Произведение цифр числа", num, ":", res)  # не смогла убрать пробел перед двоеточием.
print("Средне арифметическое: ", res2)



