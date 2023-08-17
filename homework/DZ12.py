

def avg(fn):
    def wrap(*args):
        print("Среднее арифметическое: ", fn(*args) / len(args))

    return wrap


@avg
def summa(*args):
    print("Сумма чисел: ", sum(args))
    return sum(args)


summa(2, 3, 3, 4)



