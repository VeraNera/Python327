
# Задача № 1
students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]

res = sorted(students, key=lambda item: item['name'])
res2 = sorted(students, key=lambda item: item['final'], reverse=True)

print(res)
print(res2)

# Задача № 2

nums = [3, 5, 7, 3, 9, 5, 7, 2]

b = list(map(lambda t: t ** 2, [3, 5, 7, 3, 9, 5, 7, 2]))
a = list(map(lambda t: t ** 3, [3, 5, 7, 3, 9, 5, 7, 2]))

print()
print(b)
print(a)