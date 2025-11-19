import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

try:
    df = pd.read_csv('comptagevelo2010.csv', 
                     parse_dates=['Date'], 
                     dayfirst=True, 
                     index_col='Date')
    
    df_numeric = df.select_dtypes(include=['number'])
    
    print("--- Основні характеристики ---")
    print(df_numeric.head())
    print("-" * 30)

    total_cyclists = df_numeric.sum().sum()
    print(f"Загальна кількість велосипедистів за рік: {int(total_cyclists)}")

    print("\n--- Кількість по велодоріжках ---")
    print(df_numeric.sum())

    monthly_data = df_numeric.resample('ME').sum()
    
    selected_paths = ['Berri1', 'Maisonneuve_1', 'Maisonneuve_2']
    
    print("\n--- Найпопулярніший місяць ---")
    for path in selected_paths:
        if path in monthly_data.columns:
            max_date = monthly_data[path].idxmax()
            max_val = monthly_data[path].max()
            month_name = max_date.strftime('%B')
            
            print(f"{path}: {month_name} (Кількість: {int(max_val)})")
        else:
            print(f"Увага: Доріжка {path} не знайдена в даних.")

    plt.figure(figsize=(12, 6))
    monthly_data['Berri1'].plot(kind='bar')
    plt.title("Завантаженість велодоріжки Berri1 по місяцях (2010)")
    plt.xlabel("Місяць")
    plt.ylabel("Кількість")
    
    plt.xticks(range(len(monthly_data)), 
               [d.strftime('%b') for d in monthly_data.index], 
               rotation=45)
    
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Виникла помилка: {e}")