n = int(input("Введіть кількість елементів масиву: "))
arr = []

print(f"Введіть {n} елементів масиву:")
for i in range(n):
    arr.append(float(input(f"Елемент {i+1}: ")))

print("Масив:", arr)
print("Максимальний елемент масиву:", max(arr))

