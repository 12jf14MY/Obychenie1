# Дано три случайных списка, необходимо найти в этих списках одинаковые числа
# и определить чья сумма чисел больше четных или нечетных
# import random
#
# a = set([random.randint(1, 20) for i in range(10)])
# b = set([random.randint(1, 20) for i in range(10)])
# c = set([random.randint(1, 20) for i in range(10)])
# print(a, '\n', b, '\n', c)
#
# print('Одинаковые числа', a & b & c)
#
# for i in a:
#     f = 0
#     nf = 0
#     if i % 2 == 0:
#         print('четное', i)
#         f += i
#     if i % 2 != 0:
#         print('нечетное', i)
#         nf += i
# print(nf, f)
# if nf > f:
#     print('нечетные', nf, 'больше четных', f)
# else:
#     print('четные', f, 'больше нечетных', nf)


# После переписи населения есть список фамилий. Вывести фамилии и их количество повторений.
# Сколько всего разных фамилий.

# import random
#
# a = [random.randint(1, 90) for i in range(100)]
# print(a)
# print('количество разных фамилий', len(set(a)))
# print('без повторений', set(a))
# b = ()
# for i in a:
#
#     if i not in b:

# Спортлото 6 из 36
# Игрок имеет билет с номерами от 1 до 36, он выбирает на нем (вводит в ручную), какие 6 номеров, по его предположению, выпадут.
# За 2 совпавших номера выигрыш составляет 50р., 3 совпавших - 150р., 4 совпавших - 1 000р.,
# 5 совпавших - 10 000р., 6 совпавших - 300 000р.
# После проведения розыгрыша выводятся выпавшие номера, выводится билет с отмеченными номерами, выводятся
# совпавшие номера, их количество и выигрыш.

# import random
#
# a = set([random.randint(1, 36) for i in range(36)])
# x = {random.randint(1, 36) for i in range(6)}  # выигрышные номера
# print(a)
# print(x)
# p = 0
# c = set()
# while p != 6:
#     b = int(input('введите число '))
#     if 0 < b < 37:
#         p += 1
#         c.add(b)
#     else:
#         (print('меньше 36 должно быть'))
# print(c)
#
# print('совпадения чисел', len(x & c), ' раза', x & c)




# try:
#     a = 100 / 0
# except ZeroDivisionError:
#     a = 0
# print(a)
#
# try:
#
#     int('asd')
# except Exception as e:
#     print('оiибка', e)

# dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = dict['d']
# except KeyError:
#     print(' ключа не существует')
#
# list = [1, 2, 3, 4, 5]
# try:
#     list[6]
# except IndexError:
#     print(' этого индекса нет в списке')


# dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = dict['d']
# except KeyError:
#     print(' ключа не существует')
# except IndexError:
#     print(' этого индекса нет в списке')
# except:
#     print('произошла другая ошибка')
#
# dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = dict['d']
# except (IndexError, KeyError):
#     print('роизошла ошибка IndexError или KeyError')
#
# finally:
#     print('оепратор finally выполнен ')

a = int(input('1: '))
b = int(input('2: '))

try:
    c = a / b
except ZeroDivisionError:
    c = 0
    print('деление на 0')
else:
    print(c)
    d = c ** 2
    print(d)
finally:
    print(' finally')
