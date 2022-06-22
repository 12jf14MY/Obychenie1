import sqlite3

conn = sqlite3.connect('film.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, release_year  INT, genre TEXT) ''')
conn.commit()
cursor.execute('''SELECT*FROM movies''')
k = cursor.fetchall()
print(k)

def dob_film():
    a = input('Введите название фильма: ')
    b = input('Введите год релиза: ')
    c = input('Введите жанр: ')
    cursor.execute('''INSERT INTO movies(name, release_year, genre) VALUES (?,?,?)''', (a,b,c))
    conn.commit()
    cursor.execute('''SELECT * FROM movies''')
    k = cursor.fetchall()
    print(k)

def info():
    cursor.execute('''SELECT * FROM movies''')
    k = cursor.fetchall()
    for i in k:
        s = ','.join([str(s) for s in i])
        print(s)

def f_id():
    movie_id = input('Введите id интересующего фильма: ')
    cursor.execute('''SELECT*FROM movies WHERE movie_id=?''', (movie_id,))
    m = cursor.fetchall()
    print(m)

while True:
    print('Вы можете:\n 1 - Добавить фильм\n 2 - Получить сведения р всех фильмах\n 3 - Получить сведения о фильме по id\n 0 - Выход ')
    person = input('Введите число соответствующего пункта: ')
    if person == '1':
        dob_film()
    elif person == '2':
        info()
    elif person == '3':
        f_id()
    elif person == '0':
        break