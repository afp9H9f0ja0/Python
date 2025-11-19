import matplotlib.pyplot as plt
import numpy as np

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

ukraine_data = [12450, 14200, 18500, 21000, 45000, 32000, 28000, 24500, 22000, 19500]

poland_data = [18000, 16500, 15000, 14200, 13500, 12000, 11500, 14000, 15500, 16000]

plt.figure(figsize=(10, 6)) 

plt.plot(years, ukraine_data, label='Ukraine', color='blue', linewidth=2, marker='o')
plt.plot(years, poland_data, label='Poland', color='red', linewidth=2, marker='s')

plt.title('Children out of school, primary (2010-2019)', fontsize=15)
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Number of children', fontsize=12, color='black')

plt.legend()
plt.grid(True)
plt.xticks(years) 
plt.show()


print("\nДоступні країни для побудови діаграми: Ukraine, Poland")
country_name = input("Введіть назву країни англійською (Ukraine або Poland): ").strip()

plt.figure(figsize=(10, 6)) 

if country_name == "Ukraine":
    plt.bar(years, ukraine_data, color='blue', label='Ukraine')
    plt.title(f'Statistics for {country_name}', fontsize=15)
    plt.ylabel('Number of children', fontsize=12)
    
elif country_name == "Poland":
    plt.bar(years, poland_data, color='red', label='Poland')
    plt.title(f'Statistics for {country_name}', fontsize=15)
    plt.ylabel('Number of children', fontsize=12)
    
else:
    print("Невірна назва країни або немає даних для цієї країни.")
    plt.text(0.5, 0.5, 'No data for this country', fontsize=20, ha='center')

plt.xlabel('Year', fontsize=12)
plt.xticks(years)
plt.grid(axis='y') 
plt.legend()
plt.show()