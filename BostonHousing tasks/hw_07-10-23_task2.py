import pandas as pd

# Загрузка данных
data = pd.read_csv('BostonHousing.csv')

# Группировка данных по количеству комнат
grouped_data = data.groupby('rm')

# Нахождение среднего количества комнат и стоимости для каждой группы
average_data = grouped_data[['rm', 'medv']].mean()

print(average_data)