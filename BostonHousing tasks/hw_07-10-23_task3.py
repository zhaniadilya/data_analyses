import pandas as pd

# Загрузка данных
data = pd.read_csv('BostonHousing.csv')

# Нахождение записи с максимальной стоимостью
max_price = data[data['medv'] == data['medv'].max()]

print(max_price)