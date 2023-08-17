
# через локальную переменную
def outer(a, b, c):
    def inner(x, y):
        return x * y

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))

# через глобальную
d = [2, 4, 6]
f = [5, 8, 2]
j = [1, 6, 8]


def square(y):
    def inner(n, m):
        return n * m

    s = 2 * (inner(y[0], y[1]) + inner(y[0], y[2]) + inner(y[1], y[2]))
    return s


print(square(d))
print(square(f))
print(square(j))




