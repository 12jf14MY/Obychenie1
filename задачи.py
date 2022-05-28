# Необходимо написать программу, которая требует у пользователя
# ввести целое число и проверяет чётное оно или нет

# пользователь вводит число
a = input()

# преобразовываем его к целочисленному типу
a = int(a)

# оператор % возвращает остаток от деления,
# чётные числа нацело делятся 2,
# т.е остаток от деления равен 0.
# Нечётные числа имеют остаток, равный 1.

if a % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")



a = int(input("Введите номер пальца: "))

if a == 1:
    print("Большой палец")
elif a == 2:
    print('Указательный палец')
elif a == 3:
    print('Средний палец')
elif a == 4:
    print('Безымянный палец')
elif a == 5:
    print('Мизинец')
else:
    print('Нет соответствий')


a = 0
if a > 1:
    print("а > 1 ")
if True:
    print("Hello!")



a = int(input())
b = int(input())
c = int(input())
if a > 0 and b < 0:
    print("and")
elif a > 0 or b < 0:
    print("or")
if not (c > 0):
    print("not")


# Вычислить сумму цифр случайного трёхзначного числа

import random
n = random.randint(100, 999)
print(n)
s = str(n)
a = int(s[0])
b = int(s[1])
c = int(s[2])
print(a + b + c)


# 4. Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.
a = [1, 2, 3, 2, 1, 4, 2, 5, 6, 7, 8, 89, 2, 5, ]
b = []
for i in a:
    if i count(2):
    print(d)
b.append(i)
print(b)


a = 1
for i in range(1, 8, 2):
    print(i, end='__')
    a = a * i
    print('*', a, '=', a)
print('Результат:', a )



a = [1, 2, 2, 2, 4, 6, 8, 9, 8, 1, 1]
b = []
for i in a:
    d = a.count(i)
    if d > 2:
        print('Цифра', i, ' повторяется: ', d)
        b.append(i)
        #a.remove(i)
print(b)


# Практическое 1 Пользователь вводит строку и один символ. Программа должна вывести на экран строку без этого символа.
# Например: «Я учу программирование» символ «о»
# Результат «Я учу прграммирвание».

a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    if i != b:
        c += i
        print(c)
print('Результат: ', c)


# Практическое 2 Вводится начало, конец и шаг последовательности, нужно вывести на экран данную последовательность чисел.
a = int(input('Введите начало: '))
b = int(input('Введите конец : '))
c = int(input('Введите шаг : '))
for i in range(a, b, c):
    print(i)



# Практическое 1 Вывести на экран квадраты всех целых чисел от 1 до 10.
i = 1
while i <= 10:
    print(i ** 2)
    i += 1

# Практическое 2 Перемножить все чётные значения в диапазоне от 1 до 125; результат вывести на экран.
i = 1
result = 1
while i <= 125:
    if i % 2 == 0:
        result *= i
    i += 1
print(result)


# Практическое 3 Вывести числа от 1 до 15 в порядке убывания
i = 15
while i != 0:
    print(i)
    i -= 1

# Практическое 5 Необходимо, чтоб программа выводила на экран вот такую последовательность(не использовать готовый массив):
# 7 14 21 28 35 42 49 56 63 70 77 84 91 98
# Добавить в массив и найти его длину.

a = 0
mas = []
while a < 98:
    a += 7
    mas.append(a)

print(mas, 'Длина: ', len(mas))

# # Перемножить все нечётные значения в диапазоне от 1 до 100
pr = 1

for i in range(1, 101):
    if i % 2 != 0:
        pr *= i
print(pr)
# # Записать в массив все числа в диапазоне от 1 до 500 кратные 5

mas = []

for i in range(1, 501):
    if i % 5 == 0:
        mas.append(i)
print(mas)

# # Вывести на экран все чётные значения в диапазоне от 1 до 497.
for i in range(1, 497):
    if i % 2 == 0:
        print(i)

# Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.
mas_1 = [1, 5, 3, 5, 1]
mas_2 = []
for i in mas_1:
    if mas_1.count(i) >= 2 and i not in mas_2:
        mas_2.append(i)
print(mas_2)

# Практическое 1
# Дан произвольный список.
# Представьте его в обратном порядке.
# 1 вариант
my_list = [2, 4, 8]
print(my_list[::-1])

# 2 вариант
my_list = [2, 4, 8]
my_list.reverse()
print(my_list)

# Практическое 2
# Дан список некоторых целых чисел, найдите значение 20
# в нем и, если оно присутствует, замените его на 200.
# Обновите список только при первом вхождении числа 20.
list1 = [5, 10, 15, 20, 25, 50, 20]
print("Список: \n", list1)
ind = list1.index(20)
list1[ind] = 200
print("Изменённый список: \n", list1)

# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
a = input('Введите текст: ')
gl = 0
sogl = 0
for i in a:
    if i in "aeoiu":
        gl += 1
    else:
        sogl += 1
print("Гласных: ", gl, "Согласных: ", sogl)


# print('Введите три числа: ')
# a = int(input())
# b = int(input())
# c = int(input())
#
# if b < a < c or c < a < b:
#     print('Среднее:', a)
# elif a < b < c or c < b < a:
#     print('Среднее:', b)
# else:
#     print('Среднее:', c)
#
 a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
#
# if a > b and a < c:
#     print('Среднее число:', a)
# elif b > a and b < c:
#     print('Среднее число:', b)
# else:
#     print('Среднее число:', c)
#
# d = [a, b, c]
# d.sort()
# print('Среднее число:', d[1])


print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
print(arr)
arr.sort()
print(arr)
print('Среднее:', arr[1])




 Практическое 3

mas = [1, 3, 4, 5, 6, 7, 8]
count = 0
count_2 = 0
for i in mas:
    if i % 2 == 0:
        count += 1
    else:
        count_2 += 1
print("Чётных: ", count, "Нечётных:", count_2)
sum = 0
pr = 1
if count > count_2:
    for i in mas:
        sum += i
    print("Сумма: ", sum)
else:
    pr = mas[0] * mas[2] * mas[5]
    print("Произведение: ", pr)


a = int(input('Введите число: '))
b = str(a)
b = b[::-1]
b = int(b)
print(b)

# Вводится строка. Удалить из нее все пробелы.
# После этого определить,является ли она палиндромом
# (перевертышем), т.е. одинаково пишется как с начала,
# так и с конца

s = input()
# Метод split разбивает строку на части списка
s = s.split()
# объединение списка строк с разделителем "пробел"
s = ''.join(s)
print(s)

# Выполняем срез и переворачиваем слово
if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


# s = input()
# n_s = s.replace(' ', '')
# # Выполняем срез и переворачиваем слово
# if n_s == n_s[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")



#Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент.

import random

a = [random.randint(0, 100) for i in range(10)]
a = tuple(a)
print(a)
print('max ', max(a), 'min ', min(a))




# Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа, создав тем самым третий кортеж.
# Выведите на экран третий кортеж и количество нулей в нем.
import random

a = tuple(random.randint(0, 5) for _ in range(10))
b = tuple(random.randint(-5, 0) for _ in range(10))
c = a + b
print(c, '\n Количество нулей:', c.count(0))



# Вывести данные кортежа без скобок, через запятую.
# Примечание: используйте кортеж строк

a = ('one', 'two', 'three')

c = ' '.join(a)
# c = ','.join([str(i) for i in a])
print(c)

#
# Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей
A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
s_A = sum(A)
s_B = sum(B)
if s_A > s_B:
    print("Сумма больше в кортеже - A")
else:
    print("Сумма больше в кортеже - B")

print('min A', min(A), 'Номер - ', A.index(min(A)) + 1)
print('min B', min(B), 'Номер - ', B.index(min(B)) + 1)

print(s_B)


# Операция not in - определение отсутствия ключа в словаре
# Формирование словаря слов с их числовым эквивалентом
#
# # 1. Сформировать пустой словарь
# Words = dict()  # Words = {}
#
# # 2. Ввести количество слов в словаре
# count = int(input("Количество слов в словаре: "))
#
# # 3. Цикл добавления слов
# i = 0
# while i < count:
#     print("Ввод слов")
#     wrd = input("Слово:")
#     value = int(input("Значение: "))
#
#     # Если ключа wrd нет в словаре, то добавить пару [wrd:value]
#     if wrd not in Words:
#         Words[wrd] = value
#     i = i + 1
# # Вывести сформированный словарь
# print(Words)

# Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person
person = dict(zip(['name', 'age', 'city'], ['yury', 39, 'Minsk']))
print(person)
print(person['age'])


# 2. Значениями словаря могут быть и списки.
# Допишите словарь с ключами BMW, Tesla
# и списками из 3х моделей в качестве значений.
models_data = {"BMW": ["Model_1","Model_2","Model_3"],
               "Tesla": ["Modes S", "Model A", "Model B"]}
print(models_data["Tesla"][0], models_data["Tesla"][2])
print(models_data["BMW"][0], models_data["BMW"][2])



# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

my_dictionary = {'data1': 375, 'data2': 567, 'data3': 37, 'data4': 21}
result = 1
for key in my_dictionary:
    result = result * my_dictionary[key]
print(result)


st = []
num = []

a = {1, 42, 'a', 'asd', 5, 6, 7, 2, 2, 2}
for i in a:
    if type(i) is int:
        num.append(i)
    elif type(i) is str:
        st.append(i)
num.sort()
st.sort(key=len)
print(num, st)

# 1. Создаем изменяемое множество
st = {'it', 'is', 'set', 1}

# 2. Создаем неизменяемое множество
frozen_st = frozenset({'it', 'is', 'frozen', 'set', 2})

# 3. Выполняем операцию объединения созданных множеств
# Результатом объединения будет множество, содержащее все элементы обоих множеств(без дубликатов)
union = st | frozen_st
# Результат: {'frozen', 1, 2, 'set', 'it', 'is'}

# 4. Выполняем операцию пересечения созданных множеств
# Результатом пересечения будет множество, содержащее элементы, присутствующие одновременно в обоих множествах
intersection = st & frozen_st
# Результат: {'it', 'se', 'is'}

goods = {"Apple": [4.5, 10],
         "Orange": [6.2, 5],
         "Pineapple": [10.0, 1],
         "Mango": [7.5, 2],
         "Banana": [3.8, 10]}

for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])
cost = 0
while True:
    good = input("What? (n - nothing) ")
    if good == 'n' or good not in goods.keys():
        break
    qty = int(input("How many? "))
    if qty > goods[good][1]:
        print("We don't have so much.")
        continue
    cost += goods[good][0] * qty
    goods[good][1] -= qty
print("Price:", cost)
print('___________________________________')
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])


a = [i for i in range(36)]
print(a)

new_a = set()

while len(new_a) < 6:
    c = random.choice(a)
    new_a.add(c)

print(new_a)


# Введите два числа с клавиатуры. Поделите одно на другое. Обработайте ошибку деления на ноль, если
# ошибок нет, то результат деления возвести в квадрат. Также используйте оператор finally.
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except ZeroDivisionError:
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Конец.")
