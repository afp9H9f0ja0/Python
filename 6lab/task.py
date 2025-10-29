students = {
    "Демченко Станіслав Сергійович": {
        "група": "КН-44",
        "курс": 2,
        "предмети": {
            "Програмування": 12,
            "Математика": 10,
            "Історія": 9
        }
    },
    "Красуля Ілля Ігорович": {
        "група": "КН-44",
        "курс": 2,
        "предмети": {
            "Програмування": 11,
            "Математика": 12,
            "Історія": 10
        }
    },
    "Милка Данило Дмитрович": {
        "група": "КН-44",
        "курс": 2,
        "предмети": {
            "Програмування": 8,
            "Математика": 9,
            "Історія": 7
        }
    },
    "Олейнікова Ангеліна Андріївна": {
        "група": "КН-44",
        "курс": 2,
        "предмети": {
            "Програмування": 10,
            "Математика": 10,
            "Історія": 11
        }
    },
    "Слухай Ярослав Миколайович": {
        "група": "КН-44",
        "курс": 2,
        "предмети": {
            "Програмування": 7,
            "Математика": 6,
            "Історія": 8
        }
    }
}

def print_all(data):
    """Виведення всіх даних словника"""
    print("\nІнформація про студентів:\n")
    for name, info in data.items():
        print(f"{name}: група {info['група']}, курс {info['курс']}")
        for subj, mark in info["предмети"].items():
            print(f"   {subj}: {mark}")
        print("-" * 40)
    input("Press Enter to continue...")

def add_student(data):
    """Додавання нового студента"""
    try:
        name = input("Введіть ПІБ студента: ")
        group = "КН-44"  # група фіксована
        course = int(input("Введіть курс: "))

        subjects = {}
        while True:
            subj = input("Введіть назву предмету (або Enter для завершення): ")
            if subj == "":
                break
            mark = int(input(f"Введіть оцінку з предмету '{subj}': "))
            subjects[subj] = mark

        data[name] = {"група": group, "курс": course, "предмети": subjects}
        print(f"Додано студента: {name}")
    except Exception as e:
        print("Помилка при додаванні:", e)
    input("Press Enter to continue...")

def delete_student(data):
    """Видалення студента за ПІБ"""
    name = input("Введіть ПІБ студента, якого потрібно видалити: ")
    if name in data:
        del data[name]
        print(f"Студента {name} видалено.")
    else:
        print("Помилка: студента не знайдено.")
    input("Press Enter to continue...")

def sort_by_name(data):
    """Сортування словника за ПІБ студента (алфавітно)"""
    print("\nСписок студентів (відсортовано за ПІБ):\n")
    for name in sorted(data.keys()):
        print(name)
    input("Press Enter to continue...")

def find_best(data):
    """Знаходження студента з найвищим середнім балом"""
    best_name = None
    best_avg = 0
    for name, info in data.items():
        avg = sum(info["предмети"].values()) / len(info["предмети"])
        if avg > best_avg:
            best_avg = avg
            best_name = name
    print(f"\nНайвищий середній бал у студента {best_name}: {best_avg:.2f}")
    input("Press Enter to continue...")

def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Вивести всі дані словника")
        print("2 - Додати нового студента")
        print("3 - Видалити студента")
        print("4 - Відсортувати список за ПІБ")
        print("5 - Визначити студента з найвищим середнім балом")
        print("0 - Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            print_all(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            sort_by_name(students)
        elif choice == "5":
            find_best(students)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
