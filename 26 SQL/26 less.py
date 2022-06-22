# # Обновление базы данных в таблице
# t=3
# cursor.execute('''UPDETE tab_1 SET col_1='world' WHERE id=?''',(t,))
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)



#=====================================================================================================

# Создайте новую Базу данных Поля: id, 2 целочисленных поля Целочисленные поля
# заполняются рандомно от 0 до 9 Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите эту запись, если
# нечётное, то обновите данные в ней на (2,2)
# import sqlite3
# import random
#
# # Импортируем библиотеку
# conn = sqlite3.connect('name3.db')
#
# # Создать объект, курсор,
# # который позволяет взаимодействовать с БД
# cursor = conn.cursor()
#
# # Создадим таблицу, с двумя числовыми полями(колонками)
# cursor.execute('''
# CREATE TABLE if NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER) ''')
# i = 0
# x = random.randint(1, 9)
# y = random.randint(1, 9)
#
# # Вставляем числа в таблицу
# cursor.execute(''' INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (x, y))
# conn.commit()
#
# cursor.execute('''Select id FROM tab_1''')
# k = cursor.fetchall()
# print('список кортежей :', k)
#
# r = random.choice(k)
# print('Random id:', *r)
#
# cursor.execute('''Select col_1, col_2 From tab_1 WHERE id=?''', (r))
# ou = cursor.fetchall()
# print('Values:', ou)
# n = []
# for i in ou:
#     print(i)
#     for j in i:
#         print(j)
#         n.append(j)
# if n[0] % 2 == 0 and n[1] % 2 == 0:
#     cursor.execute('''Delete From tab_1 Where id=?''', (r))
#     conn.commit()
# else:
#     cursor.execute('''Update tab_1 Set col_1 = 2, col_2 = 2 Where id=?''', (r))
#     conn.commit()
# cursor.execute('''Select id, col_1, col_2 FROM tab_1''')
# ou = cursor.fetchall()
# print(ou)
#
#
#
# #============================================================================
#
# import sqlite3
#
# conn = sqlite3.connect('test2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT ) ''')
# conn.commit()
#
#
# class A:
#     def fun(self, a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             print('INSERT 3')
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#             conn.commit()
#         elif a is not None and type(b) is int and c is None:
#             print('DELETE')
#             cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
#             conn.commit()
#         elif a is not None and b is not None and type(c) is int:
#             print('UPDATE')
#             cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
#             conn.commit()
#
# a = A()
# a.fun('c',1,2)
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)


#===============================================================================
# Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей
# записи на: hello world с помощью UPDATE*Записать данные с таблицы
# в файл в три колонки. Первая – id, вторая и третья с данными.


import sqlite3
# создаем базу данных

conn = sqlite3.connect('zad3.db')
# создаем объект cursor,который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# создадим таблицу с 2мя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('wwww','qqqq')''')
conn.commit()
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('aaaa','ssss')''')
# conn.commit()
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('zzzz','xxxxx')''')
# conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    c = ','.join([str(x) for x in i])
    print(c)


conn = sqlite3.connect('test3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT ) ''')
conn.commit()

cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

cursor.execute('''UPDATE tab_1 SET col_1='HELLO WORLD' WHERE id=3''')
conn.commit()
print(k)




with open('1.txt', 'w') as f:
    for i in k:
        s = ','.join([str(s) for s in i])
        f.write(s + '\n')