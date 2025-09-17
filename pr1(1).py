# Завдання 1

a = int(input("Введіть a: "))
while a < 1 or a > 100:
    a = int(input("Введіть a ще раз (1..100): "))

b = int(input("Введіть b: "))
while b < 1 or b > 100:
    b = int(input("Введіть b ще раз (1..100): "))

if a > b:
    X = a * b - 3
elif a == b:
    X = 2
else:
    X = (a ** 3 + 1) / b

print("Результат обчислення: X =", X)
