print("Задание 1")
a = int(input("Размер коллекции:"))
b = []
for c in range(a):
    d = input("Введите число:" )
    b.append(d)
print("Заполненная коллекция:")
print(b)

print("Задание 2")
a = int(input("Введите число:"))
b = [0] * a
for c in range(a):
    b[c] = str(c)
b[-1], b[0] = b[0], b[-1]
for c in range(1, a - 1):
    d = a - c - 1
    b[d], b[c - 1] = b[c - 1], b[d]
print(*b)
