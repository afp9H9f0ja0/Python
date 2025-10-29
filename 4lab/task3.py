def insert_before():
    try:
        A = list(map(int, input('Введіть список: ').split()))
    except ValueError:
        print("Помилка: введіть лише числа.")
        return

    print(f"Початковий список: {A}")

    try:
        target_element = int(input('Введіть елемент, перед яким треба вставити: '))
        new_element = int(input('Введіть новий елемент для вставки: '))
    except ValueError:
        print("Помилка: введіть лише число.")
        return

    result = []
    inserted = False

    for x in A:
        if x == target_element and not inserted:
            result.append(new_element)
            result.append(x)
            inserted = True
        else:
            result.append(x)

    if not inserted:
        print(f"\nЕлемент {target_element} не знайдено у списку.")
    
    print(f"Результат: {result}")
    return result

insert_before()