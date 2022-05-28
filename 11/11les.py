# варианты создания словарей
# через литерал
# d = {}
# d = {'dict': 1, 'dictionry': 2}
# print(d)
#
# #через dict
# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 2), (2, 3)])
# print(d, '\n', d_2)

# через fromkeys
# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)

# генератор словарей
import random

# a = ['a', 'b', 'c']
# d = {i: random.randint(1, 10) for i in a}
# print(d)
#
# d_2 = [3, 9, 8]
# print(d_2[0])
# print(d, d['a'])
#
# d['v'] = 20
# print(d)
#
# d['a'] = 100
# print(d)
# print(len(d))


# d = {1: 412, 'a': 23, 5: 88, 6: 'asd'}
#
# del d[5]
# print(d)

# обращение к словарю
# d = {'phone': ['pixel', 'iphone', 'nokia'],
#      'car': ['bmw', 'tesla'],
#      'dict_1': {'a': 123, 'b': 'hello'}}
# print(d)
# print(d['car'][1])
# print(d['dict_1']['b'])
# print(len(d))
#
# if 'car' in d:
#     print('car!')


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

# f = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(f)
#
# d = {'phone': ['pixel', 'iphone', 'nokia'],
#      'car': ['bmw', 'tesla'],
#      'dict_1': {'a': 123, 'b': 'hello'}}
# # for key in d:
# #     print(key)
# #     print(key, '--', d[key])
#
# for key, values in d.items():
#     print(key)
#     print(key, '--', values)


# Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person
# person = dict(zip(['name', 'age', 'city'], ['yury', 39, 'Minsk']))
# print(person)
# print(person['age'])

# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

# slovar = {'bmw': ['320', '530', 'x7'],
#           'tesla': ['Model 3', 'Model S', 'Model X']}
# print(slovar['bmw'][0:-1])
# print(slovar['tesla'][0:-1])


import random

a = ['a', 'b', 'c']
d = {i: random.randint(1, 10) for i in a}
print(d)
r = 1
s = 0
for key, values in d.items():
    print(values)
    r *= values
    s += values
print(r)
print(s)