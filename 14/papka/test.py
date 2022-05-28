# f = open('1.txt', 'r')  # Открытие  для чтения файла 1
# print(f)
# print(*f)  # вывод текстового файла в консоль
# f = open('1.txt', 'r', encoding='utf-8')  # encoding='utf-8'- для вывода русских букв
# f.close()  # закрытие файла

# ПРИМЕРЫ РАБОТЫ С ФАЙЛАМИ
# пример с finally
# f = open('1.txt', 'r', encoding='utf-8')
# try:
#     print(*f)  # либо другая работа с файлом
# finally:
#     f.close()
#
# # пример с with - as в конце файл автоматом закрывается
# with open('1.txt', 'r', encoding='utf-8')
#     print(*f)

# f = open('1.txt', 'r')
# with open('1.txt', 'r', encoding='utf-8') as f:
#     print(*f)
#     s=f.read(7)
# print(s)

# f = open('1.txt', 'r')
# with open('1.txt', 'r', encoding='utf-8') as f:
#     print(f.readline())  # читает 1 строку
#     print(f.readline())  # читает 2 строку
#     print(f.readlines())  # читает все строки
#     s = f.readlines()
# s_new=[]
# for i in s:
#     i=i.replace('\n','')
#     print(i)
#     s_new.append(i)
# print (s_new)
#
# with open('2.txt', 'w', encoding='utf-8') as f:
#     f.write('hello \nWorld') #записывает в файл

import os

# os.rename('2.txt', 'twxt.txt') #переименовывание
#
# print('текущая директория', os.getcwd())
# os.mkdir('folder')  # создание папки
# os.chdir('folder')  # смена директории
# with open('2.txt', 'w', encoding='utf-8') as f:  # создаем файл 2 в текущей директории
#     f.write('hello \nWorld')  # записываем в файл 2
# print('текущая директория', os.getcwd())
#
#
# print('текущая директория', os.getcwd())
# os.chdir('..') # возврат на директорию выше директории
# print('текущая директория', os.getcwd())
# os.makedirs('n1/n2/n3') # создание входящих папок (каскадом дерево) в директорию

# os.remove('folder/2.txt')  # удаляет файл 2 в папке folder
# os.rmdir('folder')  # удаление пустой папки. обязательно пустой!!!
# os.removedirs('n1/n2/n3')  # удалЯет папки каскадом все дерево

# Задача
# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел.

# with open('3.txt') as a:  # создаем файл  3  и открываемв текущей директории
#     # a.write('123 435 432 asd 123_df_34')  # записываем в файл 3
# with open('3.txt') as f:
#     s = f.read()
#     print(s)
#
# s = s.replace('_', ' ')
# a = s.split()
# print(a)
# s = 0
# for i in a:
#     if i.isdigit():
#         i = int(i)
#         s += i
# print(s)


# Задача
# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длинны.

with open('task_2.txt') as f:
    s = f.readlines()
print(s)
b = []
n = []
for i in s:
    i = i.replace('\n', '')
    if i.isalpha():
        b.append(i)
    elif i.isdigit():
        n.append(int(i))
print(b, n)
n.sort()
b.sort(key=len)
mas = n + b
print(mas)
