# import sqlite3
#
# # создаем базу данных
#
# conn = sqlite3.connect('name.db')
# # создаем объект cursor,который позволяет нам взаимодействовать с базой данных и добавлять записи
# cursor = conn.cursor()
# # создадим таблицу с 2мя текстовыми колонками
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# # Заполняем таблицу данными
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','word')''')
# conn.commit()
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('red','black')''')
# conn.commit()
# # запрос таблицы что бы получить все ее строки
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# # использование fetchall() для использования 1 результата 'hello'
# a='hello'
# cursor.execute('''SELECT*FROM tab_1 WHERE col_1 = 'hello' ''')
# k = cursor.fetchall()
# print(k)
# # Отсортированы относительно 2й колонки
# cursor.execute('''SELECT*FROM tab_1 ORDER BY col_2 ''')
# k = cursor.fetchall()
# print(k)
#
# cursor.execute('''SELECT*FROM tab_1 WHERE col_2 % 7 ''')
# k = cursor.fetchall()
# print(k)
# cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
# conn.commit()
# cursor.execute('''DELETE FROM tab_1 WHERE id=1 ''')
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1 ''')
# k = cursor.fetchall()
# print(k)






#=====================================================================
import sqlite3

conn = sqlite3.connect('m_name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INT)''')
n = int(input('Введите число:  '))
cursor.execute('''INSERT INTO tab_1(col_1,col_2, col_3) VALUES ('name', 'data', ?)''',  (n,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print((k))
for i in k:
    x=','.join([str(x) for x in i])
    print(x)

