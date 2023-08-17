#  ДЗ  1

# 1 способ
a = 11
b = 22
print("a:", a)
print("b:", b)
a, b = b, a
print("a:", a)
print("b:", b)

# 2 способ
a = 11
b = 22
print("a:", a)
print("b:", b)
a = a + b  # 33
b = a - b  # 22
a = a - b  # 11
print("a:", a)
print("b:", b)

# 3 способ
a = 11
b = 22
print("a:", a)
print("b:", b)
a = a * b  # 242
b = a / b  # 11
a = a / b  # 22
print("a:", a)
print("b:", b)
