import json
import os

employees = [
    {"Surname": "Іванов",    "Address": "вул. Соборна, 1",     "Position": "Менеджер"},
    {"Surname": "Петренко",  "Address": "вул. Київська, 12",   "Position": "Бухгалтер"},
    {"Surname": "Сидоренко", "Address": "вул. Миру, 5",        "Position": "Директор"},
    {"Surname": "Коваленко", "Address": "пр. Перемоги, 44",    "Position": "Інженер"},
    {"Surname": "Бондар",    "Address": "вул. Садова, 10",     "Position": "Водій"},
    {"Surname": "Ткаченко",  "Address": "вул. Лесі Українки, 7", "Position": "Секретар"},
    {"Surname": "Шевченко",  "Address": "вул. Франка, 25",     "Position": "Юрист"},
    {"Surname": "Кравчук",   "Address": "вул. Зелена, 3",      "Position": "Менеджер"},
    {"Surname": "Мельник",   "Address": "вул. Вишнева, 8",     "Position": "Прибиральник"},
    {"Surname": "Олійник",   "Address": "вул. Шевченка, 101",  "Position": "Охоронець"}
]

filename = "employees.json"
with open(filename, "w", encoding='utf-8') as file:
    json.dump(employees, file, ensure_ascii=False, indent=4)

while True:
    print("\nОберіть дію:")
    print(" 1 - Додати співробітника")
    print(" 2 - Переглянути всіх співробітників")
    print(" 3 - Знайти за першою літерою прізвища (вивести адреси)")
    print(" 4 - Вихід")
    
    choice = input("Ваш вибір: ")

    if choice == "1":
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
        
        print("\nДодавання нового співробітника:")
        surname = input("Прізвище: ")
        address = input("Адреса: ")
        position = input("Посада: ")
        
        data.append({"Surname": surname, "Address": address, "Position": position})
        
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Співробітника додано успішно!")

    elif choice == "2":
        try:
            with open(filename, "r", encoding='utf-8') as file:
                data = json.load(file)
                print("\n--- Список співробітників ---")
                for person in data:
                    print(f"{person['Surname']} - {person['Position']} ({person['Address']})")
        except FileNotFoundError:
            print("Файл не знайдено.")

    elif choice == "3":
        search_letter = input("\nВведіть першу літеру прізвища: ").strip().lower()
        
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
        
        found = False
        print(f"\nРезультати пошуку для літери '{search_letter.upper()}':")
        
        for person in data:
            first_letter = person['Surname'][0].lower()
            
            if first_letter == search_letter:
                print(f"Прізвище: {person['Surname']} | Адреса: {person['Address']}")
                found = True
        
        if not found:
            print("Співробітників з прізвищем на таку літеру не знайдено.")

    elif choice == "4":
        print("Роботу завершено.")
        break
    
    else:
        print("Невірний вибір, спробуйте ще раз.")