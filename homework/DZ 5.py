

a = [int(input("->")) for i in range(int(input('n= ')))]
b = []
for i in a:
    if i > 0:
        b.append(i)
b.sort()
print("Список: ", a)
print("Новый список из положительных элементов: ", b)
print("Наибольший элемент: ", b[-1])

a = [int(input("->")) for i in range(int(input('n= ')))]
b = []
c = a[0]
for i in a:
    if i > 0:
        b.append(i)
    if c < i:
        c = i
print("Список: ", a)
print("Новый список из положительных элементов: ", b)
print("Наибольший элемент: ", c)


