import pandas as pd
import pymysql.cursors
#import matplotlib.pyplot as plt
# Подключение к базе данных:
connection = pymysql.connect(host = '127.0.0.1',
                             user = 'root',
                             password = 'admin',
                             db ='theatre', # название базы данных
                             charset ='utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "SELECT * FROM repertoire" # запрос SQL
    # Выполнение команды запроса (Execute Query)
    cursor.execute(sql)
    rows = cursor.fetchall()# получение всех строчек
    df = pd.DataFrame(rows) # получение таблицы с данными
    #(DataFrame),
    # которая содержит результат выполнения запроса SQL
    # (то есть все записи из таблицы film)

    # Закрытие соединения (Close connection).
    connection.close()
print(df)
