import json
import matplotlib.pyplot as plt
from collections import Counter 

file_content = """
[
    {
        "Surname": "Іванов",
        "Address": "вул. Соборна, 1",
        "Position": "Менеджер"
    },
    {
        "Surname": "Петренко",
        "Address": "вул. Київська, 12",
        "Position": "Бухгалтер"
    },
    {
        "Surname": "Сидоренко",
        "Address": "вул. Миру, 5",
        "Position": "Директор"
    },
    {
        "Surname": "Коваленко",
        "Address": "пр. Перемоги, 44",
        "Position": "Інженер"
    },
    {
        "Surname": "Бондар",
        "Address": "вул. Садова, 10",
        "Position": "Водій"
    },
    {
        "Surname": "Ткаченко",
        "Address": "вул. Лесі Українки, 7",
        "Position": "Секретар"
    },
    {
        "Surname": "Шевченко",
        "Address": "вул. Франка, 25",
        "Position": "Юрист"
    },
    {
        "Surname": "Кравчук",
        "Address": "вул. Зелена, 3",
        "Position": "Менеджер"
    },
    {
        "Surname": "Мельник",
        "Address": "вул. Вишнева, 8",
        "Position": "Прибиральник"
    },
    {
        "Surname": "Олійник",
        "Address": "вул. Шевченка, 101",
        "Position": "Охоронець"
    },
    {
        "Surname": "Демченко",
        "Address": "вул. Шевченка",
        "Position": "Водій"
    }
]
"""
employees = json.loads(file_content) 

positions = [emp['Position'] for emp in employees]
position_counts = Counter(positions)

labels = list(position_counts.keys())
sizes = list(position_counts.values())

fig, ax = plt.subplots(figsize=(8, 8)) 

ax.pie(sizes, 
       labels=labels, 
       autopct='%1.1f%%', 
       startangle=90, 
       wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})

ax.set_title('Розподіл співробітників за посадами', fontsize=16)

ax.axis('equal')  

plt.show()