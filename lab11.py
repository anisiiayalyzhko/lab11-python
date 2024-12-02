import pandas as pd
import os

# Шлях до CSV файлу з даними
data_file_path = 'C:\\Users\\Anisiia\\PycharmProjects\\lab11 python\\API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_77.csv'

# Завантаження даних
data = pd.read_csv(data_file_path, skiprows=4)

# Виведення вмісту початкового файлу на екран (перші 10 рядків)
print("Вміст початкового файлу (перші 10 рядків):")
print(data.head(10))

# Вибір даних за 2010-2019 роки
columns_to_keep = ['Country Name', 'Country Code'] + [str(year) for year in range(2010, 2020)]
data = data[columns_to_keep]

# Видалення рядків із пропущеними значеннями
data_cleaned = data.dropna()

# Ініціалізація результатів
results = []

# Пошук мінімальних та максимальних значень для кожного року
for year in range(2010, 2020):
    year_str = str(year)
    min_row = data_cleaned.loc[data_cleaned[year_str].idxmin()]
    max_row = data_cleaned.loc[data_cleaned[year_str].idxmax()]
    results.append({
        'Year': year,
        'Min Country': min_row['Country Name'],
        'Min Value': min_row[year_str],
        'Max Country': max_row['Country Name'],
        'Max Value': max_row[year_str]
    })

# Створення DataFrame з результатами
results_df = pd.DataFrame(results)

# Шлях для збереження результатів
output_file_path = 'C:\\Users\\Anisiia\\PycharmProjects\\lab11 python\\inflation_results.csv'

# Використовуємо try-except для обробки помилок
try:
    # Спроба зберегти результати в файл
    results_df.to_csv(output_file_path, index=False)
    print("\nРезультати аналізу збережено у файл:", output_file_path)
except PermissionError:
    # Якщо виникає помилка доступу
    print(f"Помилка доступу! Не вдалося записати в файл: {output_file_path}")
except Exception as e:
    # Якщо виникає інша помилка
    print(f"Виникла помилка: {e}")

# Виведення вмісту результатів
print("\nРезультати аналізу (країни з мінімальною та максимальною інфляцією за кожен рік):")
print(results_df)
