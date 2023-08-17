

a = """Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели."""
count = 0
letter = "е"
for s in a.split("\n"):
    for i in s.split(" "):
        if i[0].lower() == letter:
            count += 1
print(a)
print("Количество слов: ", count)