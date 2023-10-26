import pandas as pd

# Загрузка данных
data = pd.read_csv('mtcars.csv')

# Нахождение записи с максимальной скоростью 
max_price = data[data['hp'] == data['hp'].max()]

print(max_price)