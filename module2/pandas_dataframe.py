'''Перейдите по следующей ссылке для загрузки файла (датасета): cloud.mail.ru/public/yHQU/7ely6NER5.
Ответьте на следующие вопросы на основе информации, содержащейся в этой таблице.
1. Сколько уникальных городов представлено в этом датафрейме? 
2. Сколько ресторанов в таблице специализируются на рыбе? 
3. Сколько колонок в датафрейме имеют тип данных float64? 
4. Сколько дней у ресторана с идентификатором 40065 было менее 20 успешных заказов?'''

import pandas as pd
import numpy as np
#этап 1: подготовка датафрейма
orders = pd.read_csv('orders.csv', sep = ',')
#print(orders.head(3)) #посмотрела первые несколько строк датасета, проверила правильность его загрузки

orders = orders.drop('Unnamed: 7', axis=1) #удаляю последние 2 пустых столбца
orders = orders.drop('Unnamed: 8', axis=1)
#заменяем запятые на точки и конвертируем в float
#(до этого объектов типа float64 было 0, т.к. в таблице данные записаны через запятую и поэтому становятся типа object)
for col in ['successful_orders', 'fail_orders']:
    orders[col] = orders[col].str.replace(',', '.').astype('float64')
for dtype in ['int','object']: #смотрю сколько памяти занимает датасет
    selected_dtype = orders.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print("Average memory usage for {} columns:{:03.2f} MB".format(dtype,mean_usage_mb))
'''Average memory usage for int columns:0.55 MB
Average memory usage for object columns:4.43 MB'''

#этап 2: ищу ответы
print([(col, orders[col].nunique()) for col in orders.columns])
"""[('date', 121),
('vendor_id', 1537),
('chain_id', 1063),
('city_id', 4),
('spec', 35),
('successful_orders', 193),
('fail_orders', 42)]"""
#ответ на вопрос 1: 4

print(orders[orders['spec'] == 'Рыба']['vendor_id'].nunique()) #считаем количество ресторанов со специализацией рыба
#ответ на вопрос 2: 18

print(orders.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 96118 entries, 0 to 96117
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   date               96118 non-null  object 
 1   vendor_id          96118 non-null  int64  
 2   chain_id           96118 non-null  int64  
 3   city_id            96118 non-null  int64  
 4   spec               95733 non-null  object 
 5   successful_orders  96118 non-null  float64
 6   fail_orders        96118 non-null  float64
dtypes: float64(2), int64(3), object(2)
memory usage: 5.1+ MB
None"""
#ответ на вопрос 3: 0 (т.к. мы сами поменяли последние 2 столбца на float64)

#Фильтруем по vendor_id И successful_orders < 20
filtered_orders = orders[(orders['vendor_id'] == 40065) & (orders['successful_orders'] < 20)]
print(filtered_orders['date'].count()) #считаем количество строк (дней)
#ответ на вопрос 4: 45

#ответ: 4, 18, 0, 45 
