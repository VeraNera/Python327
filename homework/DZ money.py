# n = int(input("Введите количество копеек (1-99): "))
# if 1 <= n <= 99:
#     print("У вас:", end=" ")
#     if n == 1 or n % 10 == 1 and n != 11:
#         print(n, "копейка")
#     elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")

a = int(input("Введите количество копеек (1-99): "))
kop = a
if 11 <= kop <= 14:
    print(a, "копеек")
else:
    kop = kop % 10
    if kop == 1:
        print(a, "копейка")
    elif 2 <= kop <= 4:
        print(a, "копеек")
    else:
        print(a, "копеек")



