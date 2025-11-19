import csv
import os

input_filename = "GDP_2019.csv"
output_filename = "result_GDP.csv"

flag = False

try:
    csvfile = open(input_filename, "r", encoding='utf-8')
    reader = csv.DictReader(csvfile, delimiter=";")

    print(f"Вміст файлу {input_filename}:")
    print("Country Name : 2019 [YR2019]")
    print("-" * 40)

    for row in reader:
        value = row.get("2019 [YR2019]", "N/A")
        print(f"{row['Country Name']} : {value}")

    csvfile.close()

except FileNotFoundError:
    print(f"Файл {input_filename} не знайдено! Створіть його перед запуском.")
except Exception as e:
    print(f"Виникла помилка при читанні: {e}")

try:
    csvfile = open(input_filename, "r", encoding='utf-8')
    reader = csv.DictReader(csvfile, delimiter=";")

    search_country = input("\nВведіть назву країни (або частину назви) для пошуку: ").strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Результати пошуку для: '{search_country}'")
    
    with open(output_filename, "w", newline='', encoding='utf-8') as csvfile2:
        writer = csv.writer(csvfile2, delimiter=";")
        
        writer.writerow(["Country Name", "2019 [YR2019]"])

        found_count = 0

        for row in reader:
            country_name_in_file = row["Country Name"]
            
            if search_country.lower() in country_name_in_file.lower():
                flag = True
                found_count += 1
                
                gdp_value = row.get("2019 [YR2019]", "No Data")
                
                print(f"{country_name_in_file} : {gdp_value}")
                
                writer.writerow((country_name_in_file, gdp_value))

    csvfile.close()

    if not flag:
        print(f"Країн за запитом '{search_country}' не знайдено.")
    else:
        print(f"\nЗнайдено записів: {found_count}. Результат збережено у '{output_filename}'.")

except FileNotFoundError:
    pass 
except Exception as e:
    print(f"Виникла помилка: {e}")