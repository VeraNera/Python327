

# s0 = "I am learning Python. hello, WORLD!"
# print(s0)
# print(s0.count("h"))
# print(s0.index("h"))
# print(s0.rfind("h"))
# n = ("I am learning Python. hello, WORLD!"[18:22])
# print(n)
s1 = "I am learning Python. hello, WORLD!"
print(s1)


def reverse_text_part(s, b):
    t = (s[s.index(b):s.rfind(b)+1])[::-1]
    s = s[:s.find(b)] + t + s[s.rfind(b) + 1:]
    print(s)


reverse_text_part(s1, "h")