# Завдання 3

N = int(input("Введіть N (1 < N < 9): "))

for i in range(N, 0, -1):   # від N до 1
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
