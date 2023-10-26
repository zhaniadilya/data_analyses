import pandas as pd

# Загрузка данных
data = pd.read_csv('mtcars.csv')

# Размерность данных
print("Количество записей в датасете:", len(data))
print("Количество столбцов в датасете:", len(data.columns))

# Подсчет пропущенных значений
print("Количество пропущенных значений в каждом столбце:")
print(data.isnull().sum())