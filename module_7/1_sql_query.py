#У какого продукта наибольшее количество продаж за весь период?
#Чему равна общая выручка с точностью до одного знака после запятой?

import sqlite3
import pandas as pd
#print(sqlite3.sqlite_version)
connection = sqlite3.connect('my_online_store.db')
cursor = connection.cursor()
query1 = """SELECT 
                p.product_name,           -- Выбрать название продукта (из таблицы products)
                SUM(o.quantity) as total_sales  -- Посчитать сумму quantity (количества продаж) и назвать столбец "total_sales"
            FROM 
                orders o                  -- Из таблицы orders (сокращённо называем её "o" для удобства)
            JOIN 
                products p                -- Объединить с таблицей products (сокращённо "p")
            ON o.product_id = p.product_id  -- По совпадению product_id в обоих таблицах
            GROUP BY 
                o.product_id              -- Группировать результаты по product_id (чтобы SUM работал для каждого товара)
            ORDER BY 
                total_sales DESC          -- Отсортировать по total_sales (сумме продаж) в порядке убывания (DESC)
            LIMIT 1                        -- Оставить только первую строку (товар с максимальными продажами)"""
ans1 = pd.read_sql_query(query1, connection)
print(ans1)
#product_name  total_sales
#HFvpNNVhmAUgDZ      21
query2 = """SELECT
                SUM(total_price)
            FROM
                orders"""
ans2 = pd.read_sql_query(query2, connection)
print(ans2)
print(round(145545.39, 1))
