# взяла диапазон до 100. В итоге выводится список с рандомными числами
# и второй список с уникальными.
# Если списки одинаковые, то повторяющихся чисел в нем нет

from random import randint

a = [randint(1, 100) for i in range(10)]
uniq = []
for num in a:
    if num in uniq:
        continue
    else:
        uniq.append(num)
print(a)
print()
print(uniq)


# from random import randint

a = 6
c = [randint(10, 19) for i in range(a)]
matrix = [[randint(0, 10) for x in range(a)] for y in range(a)]


def print_matrix(one):
    for row in one:
        for x in row:
            print(x, end="\t\t")
        print()
    print(c)
    print()


print_matrix(matrix)
for i in range(0, len(matrix)):
    if i == 0 or i % 2 == 0:
        matrix[i] = c

print_matrix(matrix)


