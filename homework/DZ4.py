

a = [int(input("->")) for i in range(int(input('n= ')))]
print(a)
s = 0
b = 0
for i in range(len(a)):
    if a[i] != 0:
        s += a[i]
        b += 1
print('Среднее арифметическое: ', s / b)
