import pandas as pd

# Загрузка данных
data = pd.read_csv('mtcars.csv')

# Группировка данных по количеству передач переднего хода
grouped_data = data.groupby('gear')

#print(grouped_data)