# # print("100 200 300 400".count("0"))
# print("100 200 300 400".count("0", 3, 7))
# print("100 200 300 400".count("0", 3))


# s = 'dsfklqopopqefxcmqfuoinxzlaw'
# glas = 0
# soglas = 0
# gl = 'aeoiu'
# for i in s:
#     if i in gl:
#         glas += 1
#         print(i)
#     else:
#         soglas += 1
# print('Гласные', glas)
# print('Солласные ', soglas)
# print('Согласные ', len(s) - glas)

# a = int(input('Введите число 1: '))
# b = int(input('Введите число 2: '))
# c = int(input('Введите число 3: '))
# d = [a, b, c]
# print(d)
# d.sort()
# print(d)
# print(a, "<", b, "<", c)

# a = int(input('Введите число a: '))
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

# Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
# s = [1, 2, 3, 4, 5, 6, 7]
# ch = 0
# nech = 0
# for i in s:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         nech += 1
# print('Чётные: ', ch, 'Нечётные: ', nech)
# if ch > nech:
#     sm = sum(s)
#     print('Сумма: ', sm)
# elif nech > ch:
#     pr = s[0] * s[2] * s[5]
#     print('Произведение: ', pr)


# n = input()
# reverse = n[::-1]
# print("Число с цифрами в обратном порядке:",reverse)
#
# a = int(input('Введите число: '))
# b = str(a)
# print(b[::-1])


# import random
#
# c = [random.randint(1, 100) for i in range(10)]
# print('Cгенерированные числа', c)
# print('Сумма чисел строки:', sum(c))
# print('Произведение чисел строки:', c[0] * c[1] * c[2] * c[3] * c[4] * c[5] * c[6] * c[7] * c[8] * c[9])

# #произведение
# pr = 1
# for i in c:
#     pr *= i
# print('Произведение цифр: ', pr)

# Вводиться строка. Удалить из неё все пробелы. После этого определить,
# является ли она палиндромом(перевертышем), т.е. одинаково пишется, как сначала, так и с конца

s = input('Введите строку: ')
n_s = s.replace(' ', '')
print(n_s)
if n_s == n_s[::-1]:
    print('Cрока палиндром')
else:
    print('Не палиндром')