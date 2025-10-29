def search_by_value():
    try:
        A = list(map(int, input('Введіть список (числа через пробіл): ').split()))
    except ValueError:
        print("Помилка: введіть лише числа.")
        return

    print(f"Початковий список: {A}")

    try:
        target_value = int(input('Введіть число для пошуку: '))
    except ValueError:
        print("Помилка: введіть лише число.")
        return

    found_index = -1
    
    for i in range(len(A)):
        if A[i] == target_value:
            found_index = i
            break 
            
    if found_index != -1:
        print(f"Елемент {target_value} знайдено. Його перший індекс: {found_index}")
        return found_index
    else:
        print(f"Елемент {target_value} у списку не знайдено.")
        return None

search_by_value()