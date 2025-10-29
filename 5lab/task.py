# -*- coding: utf-8 -*-

def print_all(workers):
    print("\nСписок усіх співробітників та їх адреса:\n")
    for name, address in workers.items():
        print(f"{name} — {address}")
    input("\nPress Enter to continue...")

def add_record(workers):
    try:
        name = input("Введіть прізвище співробітника: ").strip()
        address = input("Введіть адресу співробітника: ").strip()
        if name in workers:
            print("Такий співробітник вже існує!")
        else:
            workers[name] = address
            print(f"Додано запис: {name} — {address}")
    except Exception as e:
        print("Помилка при додаванні:", e)
    input("\nPress Enter to continue...")

def delete_record(workers):
    try:
        name = input("Введіть прізвище співробітника, якого потрібно видалити: ").strip()
        if name in workers:
            del workers[name]
            print(f"Видалено запис про {name}")
        else:
            print("Помилка: такого співробітника не знайдено!")
    except Exception as e:
        print("Помилка при видаленні:", e)
    input("\nPress Enter to continue...")

def print_sorted(workers):
    print("\nВідсортований список співробітників:\n")
    for name in sorted(workers.keys()):
        print(f"{name} — {workers[name]}")
    input("\nPress Enter to continue...")

def check_names(workers):
    print("\nПеревірка співробітників за прізвищами: Кузін, Куравльов, Кудін, Кульков, Кубиків.\n")
    names_to_check = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]
    found = False
    for name in names_to_check:
        if name in workers:
            print(f"{name} працює у фірмі. Адреса: {workers[name]}")
            found = True
    if not found:
        print("Жодного з перелічених співробітників не знайдено.")
    input("\nPress Enter to continue...")

def main():
    workers = {
        "Петров": "м. Харків, вул. Сумська, 22",
        "Сидоров": "м. Одеса, вул. Дерибасівська, 5",
        "Кузін": "м. Дніпро, вул. Центральна, 11",
        "Куравльов": "м. Львів, вул. Городоцька, 45",
        "Кудін": "м. Чернігів, вул. Шевченка, 7",
        "Кульков": "м. Полтава, вул. Європейська, 9",
        "Кубиків": "м. Суми, вул. Соборна, 3",
        "Гринь": "м. Запоріжжя, вул. Перемоги, 18",
        "Дрон": "м. Вінниця, вул. Київська, 14"
    }

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Вивести всі записи словника")
        print("2 - Додати новий запис")
        print("3 - Видалити запис")
        print("4 - Вивести відсортований список")
        print("5 - Перевірити наявність співробітників за прізвищем")
        print("0 - Вийти з програми")

        choice = input("Введіть пункт меню: ")

        if choice == "1":
            print_all(workers)
        elif choice == "2":
            add_record(workers)
        elif choice == "3":
            delete_record(workers)
        elif choice == "4":
            print_sorted(workers)
        elif choice == "5":
            check_names(workers)
        elif choice == "0":
            print("Завершення роботи програми...")
            break
        else:
            print("Помилка: невірний пункт меню!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
